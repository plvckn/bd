import csv
import googletrans
import time
from tqdm import tqdm
import requests
import json
import subprocess
import logging

def main():
    logging.basicConfig(format="%(levelname)s - %(asctime)s: %(message)s", datefmt= '%H:%M', level=logging.INFO)
    start = 1
    end = 5000
    counter = int(start / 1000)
    output = []
    batch_size = 10
    translator = googletrans.Translator()
    start_time = time.time()
    with open('D:\\Software\\repos\\bd\\dataset\\IMDB Dataset.csv', 'r', encoding='utf-8', errors='ignore') as r:
        reader = csv.reader(r, dialect='excel')
        
        for i, row in tqdm(enumerate(reader), total=end):
            review = row[0]
            if i > end:
                break
            elif i < start:
                continue
            try:
                translation = translator.translate(review, lang_src='en', lang_tgt='lt')
                output.append(translation.text)
            except google_trans_new.google_trans_new.google_new_transError as e:
                process = subprocess.Popen(["nordvpn", "-d"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                process.wait()
                time.sleep(7)
                process = subprocess.Popen(["nordvpn", "-c"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                process.wait()
                time.sleep(10)
                #del translator
                #translator = google_translator()
                translation = translator.translate(review, lang_src='en', lang_tgt='lt')
                output.append(translation)
            if i % 1000 == 0 and i > start:
                with open('D:\\Software\\repos\\bd\\dataset\\acc_translations\\translated_' + str(counter) + '.txt', 'w', encoding='utf-8') as w:
                    w.write('\n'.join(output))
                    counter = counter + 1
                    output = []

    print(f'finished translating {end-start} reviews in {time.time() - start_time} seconds')

            


if __name__ == "__main__":
    main()