import json
import pickle

def main():
    base_filename = 'vocab_lemmas_'
    start = 1
    end = 304

    with open(base_filename + '0.txt', 'r', encoding='utf-8') as r:
        word2lemma = json.load(r)
    
    for i in range(start, end+1):
        if i == 303:
            continue
        else:
            with open(base_filename + str(i) + '.txt', 'r', encoding='utf-8') as r:
                word2lemma.update(json.load(r))
    print(len(word2lemma))
    lowercased = {k.lower(): v.lower() for k, v in word2lemma.items()}
    with open('word2lemma_v2.txt', 'w', encoding='utf-8') as w:
        w.write(json.dumps(lowercased))
    with open('word2lemma_v2.pkl', 'wb') as w:
        pickle.dump(lowercased, w)

    with open('word2lemma.txt', 'r', encoding='utf-8') as r:
        print(len(json.load(r)))
    with open('word2lemma_v2.pkl', 'rb') as r:
        print(len(pickle.load(r)))
if __name__ == "__main__":
    main()