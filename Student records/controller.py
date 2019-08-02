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
        if selection == '4':
            model.save()
            return
        elif selection == '1':
            newgrade = view.get_grade()
            model.add_grade(student, newgrade)
        elif selection == '2':
            view.show_gpa(model.get_gpa(student))
        elif selection == '3':
            student = view.get_student()
            model.add_student(student)
        else:
            view.bad_input()


if __name__ == "__main__":
    run()
