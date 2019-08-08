def get_student():
    return input("Student name: ")

def show_menu(student):
    print()
    print("Working on student {}".format(student))
    print()
    print("Options:")
    print("1 add grade")
    print("2 show gpa")
    print("3 add student")
    print("4 quit")

def get_input():
    print()
    print("Your choice: ", end="")
    return input()
    # same as return input("Your choice: ")

def bad_input():
    print("Invalid input")

def get_grade():
    print()
    print("Your grade: ", end="")
    return input()