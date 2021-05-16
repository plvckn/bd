import re
import html
from gensim.parsing.preprocessing import * 
from gensim.utils import simple_preprocess, deaccent
from functools import reduce
from tqdm import tqdm
import os
import time
import os
from unidecode import unidecode
import constants
import json
import pandas as pd
import pickle

def read_df(path):
    return pd.read_pickle(path)

def pipeline(line, functions):
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
