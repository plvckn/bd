import logging
from time import time
from gensim.models import Word2Vec

def main():
    logging.basicConfig(format="%(levelname)s - %(asctime)s: %(message)s", datefmt= '%H:%M', level=logging.INFO)
    model = Word2Vec.load('vocab_only_accented')
    
    vocab = []

    for i, word in enumerate(model.wv.vocab):
        vocab.append((model.wv.vocab[word].index, word))

    vocab = sorted(vocab, reverse=False)
    vocab = [w[1] for w in vocab]

    length = 0
    batchsize = 49000

    output = []
    base_filename = 'accented_vocab_'
    no = 0

    for word in vocab:
        length = length + len(word)
        output.append(word)

        if length >= batchsize:
            filename = base_filename + str(no)
            with open('splits/' + filename + '.txt', 'w', encoding='utf-8') as w:
                w.write('\n'.join(output))
            length = 0
            output = []
            no = no + 1
    no = no + 1
    with open('splits/' + base_filename + str(no) + '.txt', 'w', encoding='utf-8') as w:
                w.write('\n'.join(output))
    



if __name__ == "__main__":
    main()