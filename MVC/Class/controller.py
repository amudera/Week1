import model
import view

def run():
    model.load()
    student = view.get_student()
    mainmenu(student)

def mainmenu(student):
    while True:
        view.show_menu(student)
        selection = view.get_input()
        print(selection)
        if selection == '4':
            model.save()
            return
        elif selection == '1':
            new_grade = view.get_grade()
            model.add_grade(student, new_grade)
        elif selection == '2':
            pass
        elif selection == '3':
            pass
        else:
            view.bad_input()


run()