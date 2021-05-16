import re
import html
from gensim.parsing.preprocessing import * 
from gensim.utils import simple_preprocess, deaccent
from functools import reduce
from tqdm import tqdm
import time
import os
from unidecode import unidecode



def main():
     
    output_no_preproccesing = [] 
    output_preproccesing = []
    
    num_test_lines = 10000

    #tests()
    

    with open('lt_part_3.txt', 'r', encoding='utf-8') as r, open('lt_part_3_test_v1.txt', 'w', encoding='utf-8') as w1, open('lt_part_3_clean_test_v1.txt', 'w', encoding='utf-8') as w2:
        for i, line in enumerate(r):
            output_no_preproccesing.append(line)
            #output_preproccesing.append(' '.join(simple_preprocess(line, deacc=True)))
            output_preproccesing.append(pipeline(line))
            if i == num_test_lines:
                start = time.time()

                #w1.writelines(output_no_preproccesing)
                #w2.writelines('\n'.join(output_preproccesing))

                w1.writelines(output_no_preproccesing)
                w2.write('\n'.join(output_preproccesing))

                print(f'written {num_test_lines} lines in {time.time() - start} seconds')

                return


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

#functions = [lambda x: x.lower(), clean_html_re, deaccent, unidecode, split_alphanum, strip_punctuation, remove_short_list, strip_multiple_whitespaces]
functions = [lambda x: x.lower(), clean_html_re, remove_urls, unidecode, split_alphanum, strip_punctuation, strip_multiple_whitespaces]

if __name__ == "__main__":
    main()




def tests():
    print(strip_punctuation('va cia tai "nepasiduok ... ." va cia tai parode charakteri musu vyrukai – - istrauke'))
    print('va cia tai „nepasiduok …“ va cia tai parode charakteri musu vyrukai – istrauke'.encode('ascii', 'ignore').decode())
    print(deaccent('va cia tai „nepasiduok …“ va cia tai parode charakteri musu vyrukai – istrauke'))
    print(strip_punctuation(unidecode('va cia tai „nepasiduok …“ va cia tai parode charakteri musu vyrukai – istrauke')))
    print(remove_short_list('va cia tai „nepasiduok …“ va cia tai parode charakteri musu vyrukai – istrauke'))
    print(remove_urls('dd http://vlbe.org/vlbcontent/uploads/2014/09/a.jpg 1050 1680 Sergej Sisulin http://vlbe.org/vlbcontent/uploads/2018/10/VLB_logo_web_LTDE_Short.png Sergej Sisulin2014-09-29 19:49:032014-09-29 19:54:39Poezijos popietė Štutgarte'))
