import json
import os

PATH = os.path.dirname(__file__)
DATA = "data.json"
DATAPATH = os.path.join(PATH, DATA)

data = {}

def load():
    global data
    with open(DATAPATH, "r") as file_object:
        data = json.load(file_object)

def save():
    with open(DATAPATH, 'w') as file_object:
        json.dump(data, file_object, indent=2)

def add_grade(student, grade):
    # Whole process in order:
    # student_data = data[student]
    # student_grades = student_data['grades']
    # student_grades.append(grade)
    data[student]['grades'].append(int(grade))
