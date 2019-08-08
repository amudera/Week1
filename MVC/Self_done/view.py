def get_student():
    return input("Student Name: ") #prompts for Student Name to be entered by user

def show_menu(student):
    print() #this gives a new line
    print("Working on student {}".format(student))
    print()
    print("Options: ")
    print("1 Add Grade")
    print("2 Show GPA")
    print("3 Add Student")
    print("4 QUIT")

def get_input():
    print()
    print("Your choice: ", end="")
    return input()
    #same as return input("Your choice: ")

def bad_input():
    print('Invalid Input')

def get_grade():
    print()
    print("Your grade: ",end="")
    return input() #input assigned to get grade value
