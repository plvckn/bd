import logging
from time import time
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
from gensim.utils import RULE_DEFAULT, RULE_DISCARD, RULE_KEEP

def main():
    logging.basicConfig(format="%(levelname)s - %(asctime)s: %(message)s", datefmt= '%H:%M:%S', level=logging.INFO)
    sentences = LineSentence('lt_corpus_clean_accented.txt')
    start = time()
    model = Word2Vec()
    model.build_vocab(sentences=sentences, trim_rule=trim_short)
    print(f'finished in {time() - start} seconds.')
    model.save('vocab_only_accented')


def trim_short(word, count, min_count):
    if(count >= min_count and ( len(str(word)) != 1 or str(word).isnumeric() ) ):
        return RULE_KEEP
    else:
        return RULE_DISCARD


if __name__ == "__main__":
    main()