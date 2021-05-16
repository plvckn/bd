import logging
from time import time
from gensim.models import Word2Vec
from pprint import pprint

def main():
    logging.basicConfig(format="%(levelname)s - %(asctime)s: %(message)s", datefmt= '%H:%M', level=logging.INFO)
    model1 = Word2Vec.load('model_lt')
    model2 = Word2Vec.load('model_lt_lemmatized')
    # print(len(model.wv.vocab))

    #test_similar(model)

    # test_analogies(model1)
    # test_analogies(model2)
    
    #test_similar(model1)
    #test_similar(model2)
    
    test_odd_one(model1)
    test_odd_one(model2)

def test_similar(model):
    words = ['moneta', 'sodas', 'krepsinis', 'sportuoti', 'facebook', 'playstation', 'iphone', 'paryzius']
    for word in words:
        print(f'-----{word}-----')
        pprint(model.wv.most_similar(word))



def test_analogies(model):

    analogies = [
        ['vyras', 'karalius', 'moteris'],
        ['berlynas', 'vokietija', 'paryzius'],
        ['paryzius', 'prancuzija', 'berlynas'],
        ['zaidimas', 'zaisti', 'maistas'],
        ['eina', 'ejo', 'zaidzia']
    ]
    pprint(model.wv.most_similar(positive=['moteris', 'karalius'], negative=['vyras']))
    pprint(model.wv.most_similar(positive=['paryzius', 'vokietija'], negative=['berlynas']))
    pprint(model.wv.most_similar(positive=['berlynas', 'prancuzija'], negative=['paryzius']))
    
    pprint(model.wv.most_similar(positive=['maistas', 'zaisti'], negative=['zaidimas']))


def test_similarity(model):
    pprint(model.wv.similarity('Lietuva', 'Vilnius'))
    pprint(model.wv.similarity('Prancūzija', 'Paryžius'))
    pprint(model.wv.similarity('Vokietija', 'Berlynas'))
    pprint(model.wv.similarity('pienas', 'automobilis'))

def test_odd_one(model):
    pairs = [
        ['pusryciai', 'kose', 'pietus', 'vakariene'],
        ['vysnia', 'obelis', 'gele', 'slyva'],
        ['automobilis', 'vairas', 'stabdziai', 'kamuolys'],
        ['futbolas', 'krepsinis', 'tinklaine', 'tinklinis'],
        ['teismas', 'eismas', 'advokatas', 'prokuroras']
    ]
    for pair in pairs:
        print(f'-----{pair}-----')
        pprint(model.wv.doesnt_match(pair))

if __name__ == "__main__":
    main()
