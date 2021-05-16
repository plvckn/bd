import requests
import re 
from pathlib import Path
import time 
import logging 
import json

def main():
    logging.basicConfig(format="%(levelname)s - %(asctime)s: %(message)s", datefmt= '%H:%M:%S', level=logging.INFO)

    url = 'https://klc.vdu.lt/svetaine/programos/tageris/tageris.php'
    headers = {
        'User-Agent': 'Mozilla/5.0',
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive'
    }
    # payload = {
    #     'tekstas': 'Vienas iš pirmųjų požymių, galinčių įspėti apie aukštą kraujospūdį, yra netolygios ir siauros kraujagyslės.',
    #     'tipas': 'anotuoti',
    #     'pateikti': 'L',
    #     'veiksmas': 'Rezultatas puslapyje'
    # }

    session = requests.Session()
    #result = session.post(url=url, headers=headers, data=payload)
    base_in_filename = 'accented_vocab_'
    no_in = 0
    base_out_filename = 'vocab_lemmas_'
    no_out = 0
    
    batchno = 0
    start = 304
    end = 304

    start_time = time.time()
    print(f'Beginning to parse {end-start} documents')

    for i in range(start, end+1):
        in_file = base_in_filename + str(i) + '.txt'
        out_file = base_out_filename + str(i) + '.txt'
        with open(in_file, 'r', encoding='utf-8') as r, open(out_file, 'w', encoding='utf-8') as w:
            words = r.readlines()
            words = ''.join(words)
            data = set_payload(words)
            result = session.post(url=url, headers=headers, data=data)
            words, lemmas = extract_lemmas(result.text)
            word2lemma = dict(zip(words, lemmas))
            w.write(json.dumps(word2lemma))
        if i % 10 == 0:
            batchno = batchno + 1
            print(f'processed {batchno} batches in {time.time() - start_time} seconds')
            time.sleep(5)

    print(f'finished processing everything in {time.time() - start_time} seconds')



    # pathlist = Path('D:\\Software\\repos\\bd\\dataset\\shuff-dedup\\lt\\splits').glob('**/*.txt')
    # for path in pathlist:
    #     path_name = str(path)
    #     with open(path_name, 'r', encoding='utf-8') as r, open('lemmas_vocab_1.txt', 'w', encoding='utf-8') as w:
    #         words = r.readlines()
    #         data = ' '.join(words)
    #         data = set_payload(data)
    #         result = session.post(url=url, headers=headers, data=data)
    #         print(result)
    #         print(result.text)
    #         lemmas = extract_lemmas(result.text)
    #         print(lemmas)
    #         w.writelines(lemmas)
    #     return



def extract_lemmas(data):
    word_pattern = 'word=&quot;(.+?)(?=&quot)'
    lem_pattern = 'lemma=&quot;(.+?)(?=\(|&quot;)'
    words = re.findall(word_pattern, data)
    lemmas = re.findall(lem_pattern, data)
    return (words, lemmas)

def set_payload(data):
    return {
        'tekstas': data,
        'tipas': 'anotuoti',
        'pateikti': 'L',
        'veiksmas': 'Rezultatas puslapyje'
    }


if __name__ == "__main__":
    main()

