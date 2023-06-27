def create():
    print("lets create something")

def edit():
    print("lets edit something")

def view():
    print("lets view something")

def delete():
    print("lets delete something")


def module():
    user_choice = 0
    while user_choice != 5:
        print(f'''
            Where would you like to go?
            1 - Create user
            2 - Edit user
            3 - View users 
            4 - Delete user
            5 - Exit 
        ''')
        user_choice = int(input("Please enter your choice: "))
        if user_choice == 1:s
            print("Do I even work?")
        elif user_choice == 2:
            pass
        elif user_choice == 3:
            pass
        elif user_choice == 4:
            pass
        elif user_choice == 5:
            return print('Thanks for using my CLI')
        else: 
            print("Invalid choice. Please try again.")