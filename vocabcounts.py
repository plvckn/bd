import logging
from time import time
from gensim.models import Word2Vec
from pprint import pprint


def main():
    logging.basicConfig(format="%(levelname)s - %(asctime)s: %(message)s", datefmt= '%H:%M', level=logging.INFO)
    model = Word2Vec.load('vocab_only_accented')

    print(len(model.wv.vocab))

    vocab = []

    for i, word in enumerate(model.wv.vocab):
        vocab.append((model.wv.vocab[word].index, word, model.wv.vocab[word].count))

    with open('vocab_accented_freq.txt', 'w', encoding='utf-8') as f:
        vocab = sorted(vocab, reverse=False)
        f.write('\n'.join(str(s) for s in vocab))

    

if __name__ == "__main__":
    main()