import collections
from collections import Counter
from tabulate import tabulate
import sys

def wordfreq(words):
    freq = [words.count(i) for i in words]
    print(dict(zip(words,freq)))

def reader():
    with open('article.txt','r') as file_object:
        for line in file_object:
            words = line.split()
       
            wordfreq(words)

def most_common():
    Counter = Counter(words)
    most_often = collections.Counter.most_common(words)
    print(tabulate(most_often,headers=["Words","Frequency"])

most_common()

reader()

        
