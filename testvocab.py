import logging
from time import time
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
from pprint import pprint

def main():
    logging.basicConfig(format="%(levelname)s - %(asctime)s: %(message)s", datefmt= '%H:%M', level=logging.INFO)
    model = Word2Vec.load('vocab.model')
    model_v2 = Word2Vec.load('vocab_v2')
    print(len(model.wv.vocab))
    print(len(model_v2.wv.vocab))
    

    #length_1_token_count = sum(1 for token in model.wv.vocab if len(str(token)) <= 1 )
    #length_1_token_count_v2 = sum(1 for token in model_v2.wv.vocab if len(str(token)) <= 1 )
    length_1_tokens = [token for token in model.wv.vocab if len(str(token)) == 1]
    length_1_tokens_v2 = [token for token in model_v2.wv.vocab if len(str(token)) == 1]
    #print(f'Length==1 token count: {length_1_token_count}')
    #print(f'Length==1 token count: {length_1_token_count_v2}')
    # print('V1:')
    # pprint(length_1_tokens)
    # print('V2:')
    # pprint(length_1_tokens_v2)
    print(f'V1 word count: {model.corpus_total_words} and corpus count?: {model.corpus_count}')
    print(f'V2 word count: {model_v2.corpus_total_words} and corpus count?: {model_v2.corpus_count}')
    
    #pprint(length_1_tokens)
    #print(model.wv.index2word[:1000])

if __name__ == "__main__":
    main()