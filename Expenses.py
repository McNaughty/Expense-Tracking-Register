from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from models import Base, Category, User  # Importing Base, Category, and User from the database module

class Expense(Base):
    __tablename__ = 'expenses'
    expense_id = Column(Integer, primary_key=True)
    expense_name = Column(String)
    expense_amount = Column(Float)
    cat_id = Column(Integer, ForeignKey('categories.category_id'))
    userid = Column(Integer, ForeignKey('users.user_id'))

    category = relationship("Category", back_populates="expenses")
    user = relationship("User", back_populates="expenses")

    def __init__(self, name, category, amount, expenseuser) -> None:
        self.expense_name = name
        self.category = category
        self.expense_amount = amount
        self.user = expenseuser

    # represent outputs as a string
    def __repr__(self):
        return f"Expense Entry: {self.expense_name}, {self.category.category_name}, KSH: {self.expense_amount} "
