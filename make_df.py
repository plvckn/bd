import pandas as pd


def main():
    df = pd.read_csv('D:\\Software\\repos\\bd\\dataset\\IMDB Dataset.csv', dialect='excel', encoding='utf-8')
    sentiment = df["sentiment"].values.tolist()
    with open('imdb_reviews_translated.txt', 'r', encoding='utf-8') as r:
        translated = r.readlines()
    combined = list(zip(translated, sentiment))
    
    df = pd.DataFrame(combined, columns= ['review', 'sentiment'])
    df = df[df['review'].map(lambda x: str(x.strip()) != 'Warning: Can only detect less than 5000 characters')]
    print(df.head())
    #df.to_excel('D:\\Software\\repos\\bd\\dataset\\IMDB translated.csv', 'w', encoding='utf-8')
    df.to_pickle('D:\\Software\\repos\\bd\\dataset\\IMDB translated')

if __name__ == "__main__":
    main()