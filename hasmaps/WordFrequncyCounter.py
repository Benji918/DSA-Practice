from collections import Counter

def count_word_frequency(words):
    output = {}
    count = Counter(words)
    for n in count.keys():
        output[n] = count[n]
    print(output)


words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple']
count_word_frequency(words)