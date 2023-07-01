from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from db.models import User, Investment, Transaction 
from datetime import datetime

engine = create_engine("sqlite:///db/transxceed.db") 
session = Session(engine, future=True)

def create():
    date_str = input("Please enter the date of your transaction (YYYY-MM-DD): ")
    date = datetime.strptime(date_str, "%Y-%m-%d")

    user_str = input("Please enter the user id for this transaction: ")
    investment_str = input("Please enter the investment id for this transaction: ")
    amount_str = input("Please enter the amount for this transaction: ")

    user_id = int(user_str)
    investment_id = int(investment_str)
    amount = int(amount_str)

    new_transaction = Transaction(date=date,user_id=user_id,investment_id=investment_id,amount=amount)

    session.add(new_transaction)
    session.commit()
    print("Successfully created a transaction!")

def view():
   all = session.query(Transaction).all()
   print(all)

def module():
    user_choice = 0
    while user_choice != 3:
        print(f'''
            ------TRANSACTIONS------
            Where would you like to go?
            1 - Create transaction
            2 - View transactions
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