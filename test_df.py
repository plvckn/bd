import pandas as pd
import numpy as np

def main():
    df = pd.read_pickle('D:\\Software\\repos\\bd\\dataset\\IMDB_translated_cleaned_lemma')
    # df = pd.read_pickle('IMDB translated')
    print(df['review'].values[:10])
    
def get_max(docs):
    curr_max = 0
    max_at = 0
    for i, doc in enumerate(docs):
        if len(doc.split()) > curr_max:
            curr_max = len(doc.split())
            max_at = i
    return (max_at, curr_max)


if __name__ == "__main__":
    main()