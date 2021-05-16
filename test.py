from pprint import pprint

def main():
    num_test_lines = 10001
    output = []

    with open('lt_corpus_clean_lemmatized_v4.txt', 'r', encoding='utf-8') as r, open('lt_corpus_clean_lemmatized_v4_10k.txt', 'w', encoding='utf-8') as w:
            for i, line in enumerate(r):
                output.append(line)
                if i == num_test_lines:
                    w.writelines(output)
                    #pprint(output)
                    return


if __name__ == "__main__":
    main()