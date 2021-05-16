import spacy
from pprint import pprint
from spacy.lang.lt.examples import sentences 

def main():
    nlp = spacy.load('lt_core_news_lg')


    doc = nlp('Iš medžio iškrito voverė.')
    print(doc.text)

    for token in doc:
        print(token, token.lemma, token.lemma_, token.text, token.pos_, token.dep_)



if __name__ == "__main__":
    main()