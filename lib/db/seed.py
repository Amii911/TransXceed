from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import random

from models import (User, Investment, Transaction)

fake = Faker()

engine = create_engine("sqlite:///transxceed.db")
session = Session(engine, future=True)