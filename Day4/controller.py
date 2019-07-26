import model 
import view #gives access to every function in model and view file

def run():
    model.load()
    student = view.get_student()
    mainmenu(student)

def mainmenu(student): #basically a while loop
    while True: #This loop doesnt terminate on its own. The break keyword stops the loop
        view.show_menu(student) #Print students name @ top of menu
        selection = view.get_input()
        print(selection)
        if selection == '4':
            model.save() #save before exiting
            return #exits the function. could also use /br
        elif selection =='1':
            new_grade = view.get_grade()
            model.add_grade(student,new_grade)
        elif selection =='2':
            pass
        elif selection == '3':
            pass
        else:
            view.bad_input()


run()