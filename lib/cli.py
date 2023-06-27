from helpers import (
    function_1, function_2,
    function_3, function_4,
    function_5
)

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
            function_1()
        elif user_choice == 2:
            function_2()
        elif user_choice == 3:
            function_3()
        elif user_choice == 4:
            return print('Thanks for using my CLI')
        else: 
            print("Invalid choice. Please try again.")

    
    
if __name__ == '__main__': 
    print("Welcome to TransXceed. Please use the number keys to navigate through")
    app()
    print("Come Back Again!")
