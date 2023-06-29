from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from db.models import User, Investment, Transaction 

engine = create_engine("sqlite:///db/transxceed.db") 
session = Session(engine, future=True)

def create():
    first_name = input("Please enter your first name: ")
    last_name = input("Please enter your last name: ")

    new_user = User(first_name=first_name, last_name=last_name)

    session.add(new_user)
    session.commit()
    print("Successfully created a user!")

def view():
   all = session.query(User).all()
   print(all)


def module():
    user_choice = 0
    while user_choice != 5:
        print(f'''
            Where would you like to go?
            1 - Create user
            2 - View users 
            3 - Exit 
        ''')
        user_choice = int(input("Please enter your choice: "))
        if user_choice == 1:
            create()
        elif user_choice == 2:
            view()
        elif user_choice == 3:
            return print('Going back to main menu')
        else: 
            print("Invalid choice. Please try again.")