from tqdm import tqdm

files = [
    'lt_part_1.txt',
    'lt_part_2.txt',
    'lt_part_3.txt'
]
lines_per_file = [5894130, 5807140, 903729]

with open('lt_corpus_original.txt', 'w', encoding='utf-8') as w:
    for i, fname in enumerate(files):
        with open(fname, 'r', encoding='utf-8') as f:
            for line in tqdm(f, total=lines_per_file[i]):
                w.write(line)
            w.write('\n')