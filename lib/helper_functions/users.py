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
    print("You successfully created a user!")

def edit():
    first_name = input("Enter the first name of the user you want to edit: ")
    last_name = input("Enter the last name of the user you want to edit: ")

    user = session.query(User).filter_by(first_name=first_name, last_name=last_name).first()

    if user:
        new_first_name = input("Enter the new first name: ")
        new_last_name = input("Enter the new last name: ")

        user.first_name = new_first_name
        user.last_name = new_last_name

        session.commit()
        print("User edited successfully.")
    else:
        print("User not found.")

def view():
   all = session.query(User).all()
   print(all)

def delete():
    first_name = input("Enter the first name of the user you want to delete: ")
    last_name = input("Enter the last name of the user you want to delete: ")

    user = session.query(User).filter_by(first_name=first_name, last_name=last_name).first()

    if user:
        session.delete(user)
        session.commit()
        print("User deleted successfully.")
    else:
        print("User not found.")


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
        if user_choice == 1:
            create()
        elif user_choice == 2:
            edit()
        elif user_choice == 3:
            view()
        elif user_choice == 4:
            delete()
        elif user_choice == 5:
            return print('Going back to main menu')
        else: 
            print("Invalid choice. Please try again.")