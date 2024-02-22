from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    user_id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)

class Category(Base):
    __tablename__ = 'categories'
    
    category_id = Column(Integer, primary_key=True)
    category_name = Column(String, unique=True)
    category_description = Column(String, unique=True)

class Expense(Base):
    __tablename__ = 'expenses'
    
    expense_id = Column(Integer, primary_key=True)
    expense_name = Column(String)
    expense_amount = Column(Float)
    cat_id = Column(Integer, ForeignKey('categories.category_id'))
    userid = Column(Integer, ForeignKey('users.user_id'))
    
    category = relationship("Category", back_populates="expenses")
    user = relationship("User", back_populates="expenses")

class Budget(Base):
    __tablename__ = 'budgets'
    
    budget_id = Column(Integer, primary_key=True)
    category_id = Column(Integer, ForeignKey('categories.category_id'))
    user_id = Column(Integer, ForeignKey('users.user_id'))
    budget_amount = Column(Float)
    start_date = Column(Date)
    end_date = Column(Date)
    
    category = relationship("Category", back_populates="budgets")
    user = relationship("User", back_populates="budgets")

# Table relationships
User.expenses = relationship("Expense", back_populates="user")
User.budgets = relationship("Budget", back_populates="user")
Category.expenses = relationship("Expense", back_populates="category")
Category.budgets = relationship("Budget", back_populates="category")
