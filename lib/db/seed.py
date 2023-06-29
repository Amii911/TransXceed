from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import random
import datetime

from models import User, Investment, Transaction

fake = Faker()

engine = create_engine("sqlite:///transxceed.db")
session = Session(engine, future=True)

# delete all current data
session.query(User).delete()
session.query(Investment).delete()
session.query(Transaction).delete()

# create empty array to hold new users
users = []
# create 50 users with fake first and last names
for i in range(50):
    person_1 = User(
        first_name=fake.first_name(), 
        last_name=fake.last_name(), 
        id=i)
    users.append(person_1)


investments = []
for i in range(50):
    new_invests= Investment(
        company_name=fake.company(), 
        investment_name=fake.cryptocurrency_code(),
        number_of_investments= random.randint(0, 500),
        id=i)
    investments.append(new_invests)


transactions = []
for i in range(50):
    new_transaction = Transaction(
        user_id= random.randint(0,500),
        # the id for each transaction is set to i+1 to ensure uniqueness. without it i wasnt able to seed
        id=i+1,
        date=datetime.datetime.utcnow()
    )
    transactions.append(new_transaction)

# persist new data to the database
session.add_all(users + investments + transactions)
session.commit()