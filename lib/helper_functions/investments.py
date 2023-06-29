from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from db.models import User, Investment, Transaction 

engine = create_engine("sqlite:///db/transxceed.db") 
session = Session(engine, future=True)

def create():
    print("lets create something")

def view():
   all = session.query(Investment).all()
   print(all)

def delete():
    print("lets delete something")


def module():
    user_choice = 0
    while user_choice != 5:
        print(f'''
            Where would you like to go?
            1 - Create investment
            2 - View investments 
            3 - Delete investment
            4 - Exit 
        ''')
        user_choice = int(input("Please enter your choice: "))
        if user_choice == 1:
            create()
        elif user_choice == 2:
            view()
        elif user_choice == 3:
            delete()
        elif user_choice == 4:
            return print('Going back to main menu')
        else: 
            print("Invalid choice. Please try again.")