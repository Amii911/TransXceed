from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import random

from models import (User, Investment, Transaction)

fake = Faker()

engine = create_engine("sqlite:///transxceed.db")
session = Session(engine, future=True)

# delete all current data
session.query(User).delete()

# create empty array to hold new users
users = []
# create 50 users with fake first and last names
for i in range(50):
    person_1 = User(first_name=fake.first_name(), last_name=fake.last_name(), id=i)
    users.append(person_1)
# persist new data to database
session.add_all(users)
session.commit()

