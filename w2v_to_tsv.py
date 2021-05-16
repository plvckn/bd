from gensim.models import Word2Vec

model = Word2Vec.load('model_lt')
model.wv.save_word2vec_format('model_lt_w2v_format')