from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from db.models import User, Investment, Transaction 

engine = create_engine("sqlite:///db/transxceed.db") 
session = Session(engine, future=True)

def create():
    company_name = input("Please enter the company you like to make an investment with: ")
    investment_name = input("Please enter the investments name: ")
    number_of_investments = input("How many investments would you like to add? ")

    new_investment = Investment(company_name=company_name, investment_name=investment_name, number_of_investments=number_of_investments)

    session.add(new_investment)
    session.commit()
    print("You have successfully added a new investment!")

def view():
   all = session.query(Investment).all()
   print(all)

def delete():
    investment_id = input("Enter the ID of the investment you want to delete: ")

    investment = session.query(Investment).get(investment_id)

    if investment:
        session.delete(investment)
        session.commit()
        print("Investment deleted successfully.")
    else:
        print("Investment not found.")


def module():
    user_choice = 0
    while user_choice != 5:
        print(f'''
            ------INVESTMENTS------
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