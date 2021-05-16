from numpy.core.defchararray import encode
import tensorflow as tf
from tensorflow import keras
import numpy as np
from gensim.models import KeyedVectors
import pandas as pd

def main():

    data = get_data()


    tokenizer = tf.keras.preprocessing.text.Tokenizer()
    tokenizer.fit_on_texts(data['review'])
    vocab_size = len(tokenizer.word_index) + 1
    encoded_docs = tokenizer.texts_to_sequences(data['review'])
    labels = np.asarray(encode_labels(data['sentiment'])).astype('int32')

    MAX_SEQ_LENGTH = 250
    encoded_docs = tf.keras.preprocessing.sequence.pad_sequences(encoded_docs, maxlen=MAX_SEQ_LENGTH, padding='post', truncating='post')


    
    #dataset = tf.data.Dataset.from_tensor_slices((encoded_docs, labels))
    # dataset = dataset.shuffle(ds_size)
    # train_ds = dataset.take(train_size)
    # test_ds = dataset.skip(train_size)
    # val_ds = test_ds.take(val_test_size)
    # test_ds = test_ds.skip(val_test_size)

    ds_size = len(data['review'])
    train_size = int(0.7 * ds_size)
    val_test_size = int(0.15 * ds_size)
    x_train = encoded_docs[:train_size]
    y_train = labels[:train_size]
    x_val = encoded_docs[train_size:train_size+val_test_size]
    y_val = labels[train_size:train_size+val_test_size]
    

    embeddings = load_embedding()
    embedding_matrix = get_weight_matrix(embeddings, tokenizer.word_index)

    

    
    EMBEDDING_DIM = 100
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Embedding(vocab_size, output_dim=EMBEDDING_DIM, embeddings_initializer=keras.initializers.Constant(embedding_matrix), trainable=False))
    model.add(tf.keras.layers.GlobalAveragePooling1D())
    model.add(tf.keras.layers.Dense(16, activation='relu'))
    model.add(tf.keras.layers.Dense(1, activation='sigmoid'))
    model.summary()


    model.compile(
        optimizer='adam',
        loss=tf.keras.losses.BinaryCrossentropy(from_logits=False),
        metrics=['accuracy']
    )


    batch_size = 512

    # history = model.fit(
    #     train_ds.shuffle(train_size).batch(batch_size),
    #     epochs=10,
    #     validation_data=val_ds.batch(batch_size),
    #     verbose=1
    # )

    callback = tf.keras.callbacks.EarlyStopping(monitor='loss', patience=3)

    history = model.fit(
        x_train,
        y_train,
        epochs=10,
        batch_size=batch_size,
        validation_data=(x_val, y_val),
        verbose=1,
        callbacks=[callback]
    )


    model.save('saved_model/imdb_classifier_lt_base')
    np.save('imdb_classifier_lt_base_history.npy', history)

def get_data(path='D:\\Software\\repos\\bd\\dataset\\IMDB_translated_cleaned'):
    return pd.read_pickle(path) 

def encode_labels(labels):
    return [1 if label == 'positive' else 0 for label in labels]

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

def to_tensor(data):
    return tf.constant(data)

if __name__ == "__main__":
    main()
