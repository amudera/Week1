import json
from pprint import pprint
import os

# print(__file__)

DIRECTORY = os.path.dirname(__file__)
# print(DIRECTORY)

FILENAME = "mydata.json"
FILEPATH = os.path.join(DIRECTORY, FILENAME)
# print(FILEPATH)

with open(FILEPATH, 'r') as file_object:
    data = json.load(file_object)

pprint(data)
print(type(data))