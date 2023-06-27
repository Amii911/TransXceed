from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer(), primary_key=True)
    first_name = Column(String())
    last_name = Column(String())

    def __repr__(self):
        return f'Name : {self.first_name} and {self.last_name}'


class Investment(Base):
    __tablename__ = 'investments'

    id = Column(Integer(), primary_key=True)
    company_name = Column(String())
    investment_name = Column(String())
    number_of_investments = Column(Integer())

    def __repr__(self):
        pass


class Transactions(Base):
    __tablename__ = 'tranactions'

    id = Column(Integer(), primary_key=True)
    date = Column(Integer())
    user_id = Column(Intger())

    def __repr__(self):
        pass

   