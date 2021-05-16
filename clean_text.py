import re
from gensim.parsing.preprocessing import * 
from gensim.utils import simple_preprocess, deaccent
from functools import reduce
from tqdm import tqdm
import time
import os
from unidecode import unidecode
import constants
import json
import pandas as pd

with open('splits/word2lemma.txt', 'r', encoding='utf-8') as r:
        word2lemma = json.load(r)

def main():
     
    total_lines = constants.lt_combined_lines
    batchsize = 500000
    batchno = 0
    output = []
    execution_time = time.time()


    with open('lt_corpus_clean.txt', 'r', encoding='utf-8') as r, open('lt_corpus_clean_lemmatized_v4.txt', 'w', encoding='utf-8') as w:
        for line in tqdm(r, total=total_lines):
            output.append(pipeline(line))
            if(len(output) == batchsize):
                start_write = time.time()
                w.write('\n'.join(output))
                output = []
                print(f'written batch {batchno} of {batchsize} lines in {time.time() - start_write} seconds')
                batchno = batchno+1
        w.write('\n'.join(output))

    print(f'finished execution in {time.time() - execution_time} seconds')


def read_df(path):
    return pd.read_pickle(path)

def pipeline(line):
    return reduce(lambda clean, f: f(clean), functions, line)


def clean_html_re(raw_html):
    cleanr = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
    return re.sub(cleanr, '', raw_html)

def remove_short(s):
    return s if len(s)>1 else ''

def remove_short_list(s):
    return ' '.join(s if len(s)>1 else '' for s in s.split())

def remove_urls(s):
    pattern1 = re.compile(r'http\S+')
    pattern2 = re.compile(r'www\S+')
    return re.sub(pattern2, '', re.sub(pattern1, '', s))

def word_2_lemma(line):
    return ' '.join([word2lemma.get(word.strip(), word) for word in line.split()])

functions = functions = [lambda x: x.lower(), str.strip, clean_html_re, remove_urls, unidecode, split_alphanum, strip_punctuation, strip_multiple_whitespaces]
functions_lemma = [lambda x: x.lower(), str.strip, clean_html_re, remove_urls, strip_punctuation, word_2_lemma, unidecode, lambda x: x.lower(), split_alphanum, strip_punctuation, strip_multiple_whitespaces]

if __name__ == "__main__":
    main()

