import csv
from random import randint
from pprint import pprint

ten_by_ten_rand_values = [[randint(10,99) for i in range(10)] for j in range(10)]

# list comprehension is the same as:
sample_list = []
for g in range(0, 10):
    new_list = []
    for i in range(0, 5):
        new_list.append(i)
    sample_list.append(new_list)

# print(sample_list)
sample = [i for i in range(10)]
# pprint(ten_by_ten_rand_values)
"""
with open('no_key_output.csv', 'w') as file_object:
    writer = csv.writer(file_object)
    for row in ten_by_ten_rand_values:
        writer.writerow(row)
"""
key_list = ["firstname", "lastname", "gpa"]
dict_rows = [
    {"firstname": "Carter", "lastname": "Adams", "gpa": 2.1},
        {"firstname": "Kenso", "lastname": "Trabing", "gpa": 3.2},
        {"firstname": "Greg", "lastname": "Smith", "gpa": 3.9}
]

with open('keys_output.csv', 'w') as file_object:
    writer = csv.DictWriter(file_object, key_list)
    writer.writeheader()
    for row in dict_rows:
        writer.writerow(row)

with open('no_key_output.csv', 'a') as file_object:
    writer = csv.writer(file_object)
    writer.writerow([randint(100,999) for _ in range(10)])

