from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer(), primary_key=True)
    first_name = Column(String())
    last_name = Column(String())

    transactions = relationship('Transaction', backref=backref('user'))

    def __repr__(self):
        return f'''
            Name : {self.first_name} {self.last_name}
            User Id : {self.id}
        '''


class Investment(Base):
    __tablename__ = 'investments'

    id = Column(Integer(), primary_key=True)
    company_name = Column(String())
    investment_name = Column(String())
    number_of_investments = Column(Integer())

    def __repr__(self):
        return f'''
            Company Name : {self.company_name}
            Investment Name : {self.investment_name}
            Number of Investments : {self.number_of_investments}
            Investment Id : {self.id}
        '''


class Transaction(Base):
    __tablename__ = 'transaction'

    id = Column(Integer(), primary_key=True)
    date = Column(Integer())
    user_id = Column(Integer())

    def __repr__(self):
        return f''' 
            User Id: {self.user_id}
            Transaction Id : {self.id}
        '''

   