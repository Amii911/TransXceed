from sqlalchemy import Column, Integer, Date, String, ForeignKey, Boolean
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
            User Id : {self.id}
            Name : {self.first_name} {self.last_name}            
        '''


class Investment(Base):
    __tablename__ = 'investments'

    id = Column(Integer(), primary_key=True)
    company_name = Column(String())
    investment_name = Column(String())
    number_of_investments = Column(Integer())

    def __repr__(self):
        return f'''
            Investment Id : {self.id}
            Company Name : {self.company_name}
            Investment Name : {self.investment_name}
            Number of Investments : {self.number_of_investments}            
        '''


class Transaction(Base):
    __tablename__ = 'transaction'

    id = Column(Integer(), primary_key=True)
    date = Column(Integer())
    user_id = Column(Integer(), ForeignKey("users.id"))
    investment_id = Column(Integer(), ForeignKey("investments.id"))
    amount = Column(Integer())
    

    def __repr__(self):
        return f''' 
            Transaction Id : {self.id}
            User Id: {self.user_id}            
            Investment Id: {self.investment_id}
            Amount: {self.amount}
            Date: {self.date}
        '''

   