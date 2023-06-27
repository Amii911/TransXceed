import sys
import importlib
sys.path.append('./helper_functions')

investments = importlib.import_module('investments')
users = importlib.import_module('users')
transactions = importlib.import_module('transactions')


def app():
    print('Welcome to my CLI!')
    user_choice = 0
    while user_choice != 4:
        print(f'''
            Where would you like to go?
            1 - users
            2 - investments
            3 - transactions 
            4 - exit
        ''')
        user_choice = int(input("Please enter your choice: "))
        if user_choice == 1:
            users.module()
        elif user_choice == 2:
            pass
        elif user_choice == 3:
            transactions.module()
        elif user_choice == 4:
            return print('Thanks for using my CLI')
        else: 
            print("Invalid choice. Please try again.")

    
if __name__ == '__main__': 
    print("Welcome to TransXceed. Please use the number keys to navigate through")
    app()
    print("Come Back Again!")
