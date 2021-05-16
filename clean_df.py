from cleaning_functions import *

with open('D:\\Software\\repos\\bd\\dataset\\shuff-dedup\\lt\\splits\\word2lemma_v2.txt', 'r', encoding='utf-8') as r:
        word2lemma = json.load(r)

def main():
    functions = [lambda x: x.lower(), str.strip, clean_html_re, remove_urls, unidecode, split_alphanum, strip_punctuation, strip_multiple_whitespaces]
    functions_lemma = [lambda x: x.lower(), str.strip, clean_html_re, remove_urls, strip_punctuation, word_2_lemma, unidecode, lambda x: x.lower(), split_alphanum, strip_punctuation, strip_multiple_whitespaces]
    df = read_df('D:\\Software\\repos\\bd\\dataset\\IMDB translated')
    reviews = df['review']
    sentiment = df['sentiment']

    count_before = len(reviews)
    cleaned = clean_list(reviews, functions_lemma)
    df = pd.DataFrame(list(zip(cleaned, sentiment)), columns= ['review', 'sentiment'])
    df.to_pickle('D:\\Software\\repos\\bd\\dataset\\IMDB_translated_cleaned_lemma_v2')
    if count_before != len(cleaned):
        print(f'counts do now match: {len(count_before)} <--> {len(cleaned)}')
        return
    else:
        print('counts match')

def clean_list(list, functions):
    output = []
    for review in tqdm(list, total=50000):
        output.append(pipeline(review, functions))
    return output
    
def word_2_lemma(line):
    return ' '.join([word2lemma.get(word.strip(), word) for word in line.split()])

if __name__ == "__main__":
    main()