
def main():
    corpus_total_words = 517268174
    vocab_size = 1038751

    
    sums = []
    percentages = []
    top_words = [10, 100, 1000, 10000, 100000, 1000000]
    observations = len(top_words)


    observation = 0
    sum = 0

    print(top_words[-1])

    with open('vocab_freq.txt', 'r') as f:
        for i, token_info in enumerate(f):
            count = token_info.split(',')[2][:-2]
            sum = sum + int(count)
            if i <= top_words[-1] and i == top_words[observation]:
                sums.append(sum)
                percentages.append(get_percentage(sum))
                observation = observation + 1
            elif i > top_words[-1]:
                break


    print(len(sums))
    print(len(percentages))
    sums = ["%.2f" % s for s in [s/1000000 for s in sums]]
    percentages = ["%.2f" % p for p in percentages]
    print(top_words)
    print(sums)
    print(percentages)

def get_percentage(token_counts, corpus_size=517268174):
    return token_counts / corpus_size * 100

if __name__ == "__main__":
    main()