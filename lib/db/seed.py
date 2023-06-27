from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import random

from models import (User, Investment, Transaction)

fake = Faker()

engine = create_engine("sqlite:///transxceed.db")
session = Session(engine, future=True)


session.query(User).delete()

users = []

for i in range(50):
    person_1 = User(first_name=fake.first_name, last_name=fake.last_name)
    users.append(person_1)

session.add(users)
session.commit()