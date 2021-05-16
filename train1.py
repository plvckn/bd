import logging
from time import time
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
from gensim.utils import RULE_DEFAULT, RULE_DISCARD, RULE_KEEP

def main():
    logging.basicConfig(format="%(levelname)s - %(asctime)s: %(message)s", datefmt= '%H:%M', level=logging.INFO)
    

    model = Word2Vec(
        corpus_file='lt_corpus_clean_lemmatized_v4.txt',
        )
    # model = Word2Vec.load('vocab_v2')
    # model.train(
    #     sentences=LineSentence('lt_corpus_clean.txt'),
    #     total_examples=model.corpus_count,
    #     epochs=model.epochs,
    #     )
    model.save('model_lt_lemmatized')




if __name__ == "__main__":
    main()