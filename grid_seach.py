import tensorflow as tf
from tensorflow import keras
import numpy as np
from gensim.models import KeyedVectors
import pandas as pd
import joblib
from sklearn.model_selection import GridSearchCV
from keras.wrappers.scikit_learn import KerasClassifier


def encode_labels(labels):
    return [1 if label == 'positive' else 0 for label in labels]

def create_model(vocab_size=195850, neurons=16):
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Embedding(vocab_size, output_dim=100, embeddings_initializer=keras.initializers.Constant(embedding_matrix), trainable=False))
    model.add(tf.keras.layers.GlobalAveragePooling1D())
    model.add(tf.keras.layers.Dense(neurons, activation='relu'))
    model.add(tf.keras.layers.Dense(1, activation='sigmoid'))
    model.compile(optimizer='adam', loss=tf.keras.losses.BinaryCrossentropy(from_logits=False), metrics=['accuracy'])
    return model

def load_embedding(filename='D:\\Software\\repos\\bd\\dataset\\shuff-dedup\\lt\\model_lt'):
    model = KeyedVectors.load(filename)
    vocab = model.wv.vocab
    embedding = dict()
    for word in vocab:
        embedding[word] = model.wv[word]
    return embedding

def get_weight_matrix(embedding, vocab):
    vocab_size = len(vocab) + 1
    weight_matrix = np.zeros((vocab_size, 100))
    for word, i in vocab.items():
        try:
            weight_matrix[i] = embedding[word]
        except KeyError:
            weight_matrix[i] = np.zeros(100)
    return weight_matrix


tf.config.list_physical_devices('GPU')

data = pd.read_pickle('D:\\Software\\repos\\bd\\dataset\\IMDB_translated_cleaned')

tokenizer = tf.keras.preprocessing.text.Tokenizer()
tokenizer.fit_on_texts(data['review'])
vocab_size = len(tokenizer.word_index) + 1

encoded_docs = tokenizer.texts_to_sequences(data['review'])
labels = np.asarray(encode_labels(data['sentiment'])).astype('int32')

MAX_SEQ_LENGTH = 250
encoded_docs = tf.keras.preprocessing.sequence.pad_sequences(encoded_docs, maxlen=MAX_SEQ_LENGTH, padding='post', truncating='post')

ds_size = len(data['review'])
train_val_size = int(0.9 * ds_size)
x_train_val = encoded_docs[:train_val_size]
y_train_val = labels[:train_val_size]
x_test = encoded_docs[train_val_size:]
y_test = labels[train_val_size:]

embeddings = load_embedding()
embedding_matrix = get_weight_matrix(embeddings, tokenizer.word_index)


model = KerasClassifier(build_fn=create_model, batch_size=512, epochs=10, verbose=0)

param_grid = {
    'neurons': [16, 32, 64]
}
grid = GridSearchCV(estimator=model, param_grid=param_grid, cv=3, verbose=1)
grid_results = grid.fit(x_train_val, y_train_val)

print(grid_results.cv_results_)
joblib.dump(grid_results.best_estimator_, 'D:\\Software\\repos\\bd\\grid_models\\estimator.pkl')


