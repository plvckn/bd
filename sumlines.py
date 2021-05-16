import time

start = time.time()

num_lines = sum(1 for line in open('lt_corpus_clean_lemmatized_v4.txt', mode='r', encoding='utf-8'))
print(f'num lines: {num_lines} (Counted in {time.time() - start} seconds)')