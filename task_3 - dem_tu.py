import re
from collections import defaultdict

def count_words(file_path):
    word_count = defaultdict(int)

    with open(file_path, 'r') as file:
        for line in file:
            words = re.findall(r'\b\w+\b', line.lower())
            for word in words:
                word_count[word] += 1

    return dict(word_count)

file_path = 'P1_data.txt'
res = count_words(file_path)
for word, count in res.items():
    print(word, count)
    print()
