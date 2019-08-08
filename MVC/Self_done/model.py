import json
import os 

PATH = os.path.dirname(__file__)
DATA = "data.json"
DATAPATH = os.path.join(PATH,DATA)

data = {} #this allows data variable to be used by any function that needs to use the data

def load():
    global data 
    with open(DATAPATH,"r") as file_object:
        data = json.load(file_object) #reassigned data to be whats in the file

def save():
    with open(DATAPATH,'w') as file_object:
        json.dump(data,file_object, indent=2) #saves over the json file

def add_grade(student,grade):
    # student_data = data(student)
    # student_grades = student_data('grades') #gets the key value pairs with key being grades
    # student_grades.append(grade) #adds grade to the list
    data[student]['grades'].append(int(grade))

