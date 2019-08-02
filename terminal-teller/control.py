import model
import viewm

def run():
    model.load()
    view.main_menu()

def mainmenu():
    while True:
        view.main_menu()
        selection = view.get_input()
        print(selection)
        if selection == '3':
            model.save()
            return
        elif selection == '1':
            new_account = view.create_account()
            model.gen_account()
            model.add_account()
            view.account_creation()
        elif selection == '2':
            viewm.log_in()
        else:
            view.bad_input()