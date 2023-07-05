# TransXceed

## Decription

TransXceed is a new way to track and view your investments. How exiting would it be to have a new system where you can create and delete these new investments? This application is a Command Line Interface allows users to query from a SQLAlchemy database of investments, users, and transactions. The database is set up with many-to-many relationships backrefered through the users table. Users can have many investments and users can have many transactions. 

***

## Installation

To install and run TransXceed, ensure that you have Python 3 and pip installed on your system.

1. Clone this repository to your local machine and navigate to its directory.
2. Run `pipenv install` to install all the necessary package dependencies.
3. Run `pipenv shell` to enter the virtual environment.
4. Navigate to the `lib/db` directory and run `python seed.py` to populate the database with mock data.
5. Return to the `lib` directory by running `cd ..`
6. Run `python cli.py` to start using TransXceed.


## App Functionality
Upon running the app, you will be presented with the main menu. From there, you can navigate through different options and perform various actions. Here's an overview of the available functionality:

Main Menu
1. USERS
2. INVESTMENTS
3. TRANSACTIONS 
4. EXIT
***
User Menu
1. Create user
2. Edit user
3. View users 
4. Delete user
5. List transactions for users
6. Exit 
***
Investment Menu
1. Create investment
2. View investments 
3. Delete investment
4. Exit 
***
Transaction Menu
1. Create transaction
2. View transaction
3. Exit 

## Resources
- [SQLite](https://sqlite.org/index.html) - a relational database engine that comes with Python
- [SQLAlchemy](https://www.sqlalchemy.org/) - a Python ORM package to map database tables to Python classes
- [Faker](https://faker.readthedocs.io/en/master/) - a Python package that generates fake data
- [Alembic](https://alembic.sqlalchemy.org/en/latest/) - a Python lightweight package for data mirgations 

