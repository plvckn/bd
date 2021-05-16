import re
import html
from gensim.parsing.preprocessing import * 
from gensim.utils import simple_preprocess
from functools import reduce

# Cleans text of html tags like <a></a> aswell as other html entities like '&nsbm'

def clean_html_re(raw_html):
    cleanr = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
    return re.sub(cleanr, '', raw_html)

# Convert html entities like '&nbsp' or '&gt' to their respective symbols eg.: '&gt' -> '>'

def unescape_html(raw_html): 
    return html.unescape(raw_html)


def simple_pipeline(texts):
    return reduce((lambda x: [x.lower(), strip_tags(x), unescape_html(x), strip_punctuation(x), strip_multiple_whitespaces(x)]), texts)










# main function to test pipeline functions

def main():
    
    raw_html = '<a href="wHAtever.com">some &gt; &#62; &#x3e;text a-b.c, ,</a>'
    print('unescape html:\n', unescape_html(raw_html))
    print('strip html:\n', clean_html_re(raw_html))
    print('split alphanumeric:\n', split_alphanum('42days7weeks351cars15 agent 00 7'))
    print('strip non alphanumeric:\n', strip_non_alphanum(raw_html))
    print('strip numeric:\n', strip_numeric('this1is2heck3of4aday5 365 days in 1 year'))
    print('strip html tags:\n', strip_tags(raw_html))
    print('strip html tags & unescape html:\n', unescape_html(strip_tags(raw_html)))
    print('remove punctuation:\n', strip_punctuation(raw_html))
    print('strip tags & unescape & strip punct\n', strip_punctuation(unescape_html(strip_tags(raw_html)))) # same as clean_html_re + strip punc fn
    print('strip html & strip punct:\n', strip_punctuation(clean_html_re(raw_html)))
    print('deaccent:\n', ' '.join(simple_preprocess('Aš gyvenu ąžuoliuke-medįje -cę.', deacc=True)))
    print('List:\n', ['sdf'])
    print('Simple pipeline:\n', simple_pipeline([raw_html]))

if __name__ == "__main__":
    main()