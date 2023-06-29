from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from db.models import User, Investment, Transaction 

engine = create_engine("sqlite:///db/transxceed") 
session = Session(engine, future=True)

def create():
    print("lets create something")

def view():
   all = session.query(Transaction.all())
   print(all)

def module():
    user_choice = 0
    while user_choice != 3:
        print(f'''
            Where would you like to go?
            1 - Create transaction
            2 - View transaction
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