#!/usr/bin/env python3

with open('article.txt', 'r') as f:
    data = f.readlines()
import collections
from collections import Counter

for line in data:
    words = line.split()
    Counter = Counter(words)
    most_often = collections.Counter.most_common(words)
    print(words)
