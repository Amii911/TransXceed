import sys
import importlib
sys.path.append('./helper_functions')

investments = importlib.import_module('investments')
users = importlib.import_module('users')
transactions = importlib.import_module('transactions')


def app():
    user_choice = 0
    while user_choice != 4:
        print(f'''
            Where would you like to go?
            1 - USERS
            2 - INVESTMENTS
            3 - TRANSACTIONS 
            4 - EXIT
        ''')
        user_choice = int(input("Please enter your choice: "))
        if user_choice == 1:
            users.module()
        elif user_choice == 2:
            investments.module()
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
