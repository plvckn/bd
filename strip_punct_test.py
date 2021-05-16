import string
import re
import constants
from tqdm import tqdm
import time

def main():

    output = []
    batchsize = 500000
    batchno = 0
    execution_time = time.time()

    with open('lt_part_3_clean_accented_v1.txt', 'r', encoding='utf-8') as f, open('lt_part_3_clean_accented_v2.txt', 'w', encoding='utf-8') as w:
        for line in tqdm(f, total=constants.lt_part_1_lines):
            output.append(strip_punct(line))
            if(len(output) == batchsize):
                start_write = time.time()
                w.write(''.join(output))
                output = []
                print(f'written batch {batchno} of {batchsize} lines in {time.time() - start_write} seconds')
                batchno = batchno+1
        w.write('\n'.join(output))

    print(f'finished execution in {time.time() - execution_time} seconds')


def strip_punct(s):
    return re.sub(r'[^\w\s]', '', s, re.UNICODE)

if __name__ == "__main__":
    main()

