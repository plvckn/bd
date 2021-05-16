import json

with open('splits/word2lemma.txt', 'r', encoding='utf-8') as r:
        word2lemma = json.load(r)

test = dict()

for i, (k, v) in enumerate(word2lemma.items()):
    #print(f'Žodis: {k}, lema: {v}')
    if i>70:
        test[k] = v
    if i==100:
        break

print(test)