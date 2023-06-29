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
    print("                  Let's edit a position's name!")
    print(session.query(Position).all())
    print("                  Please enter the ID of the position who's name you'd like to edit: ")
    edit_id = int(input())
    edit_id = session.query(Position).get(edit_id)
    if edit_id != None: 
        print(edit_id)
        print(f"                  What would you like the new name of {edit_id.name} to be?")
        new_name = str(input())
        print(f'''
                   OLD NAME : {edit_id.name}
                   NEW NAME : {new_name}

                Is this correct?
                --------------------------------------
                     1 : YES

                     2 : NO
        ''')
        check = int(input())
        while check != 3:
            if check == 1:
                print("                  Your changes have been saved!")
                session.commit()
                check = 3

            if check == 2:
                print("                  Oh no! Let's try that again...")
                edit()

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