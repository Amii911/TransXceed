from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer(), primary_key=True)
    first_name = Column(String())
    last_name = Column(String())


class Investment(Base):
    __tablename__ = 'investments'

    id = Column(Integer(), primary_key=True)
    company_name = Column(String())
   