import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Expense, User, Category  # Importing SQLAlchemy models

# Create SQLAlchemy engine and session
engine = create_engine('sqlite:////ExpendiTracker.db')  
Session = sessionmaker(bind=engine)
session = Session()

# Function to fetch user's expenses from the database
def fetch_user_expenses(username, session):
    try:
        user = session.query(User).filter(User.username == username).first()
        if user:
            expenses = session.query(Expense, Category.category_name).join(Category).filter(Expense.userid == user.user_id).all()
            return expenses
        else:
            print("User not found.")
            return None
    except Exception as e:
        print("Error fetching user's expenses:", e)
        return None

# Function to calculate total amount spent by the user
def calculate_total_spent(expenses):
    total_spent = sum(expense[0].expense_amount for expense in expenses)
    return total_spent

# Function to generate a pie chart of expenses by category
def generate_category_pie_chart(expenses):
    category_totals = {}
    for expense, category_name in expenses:
        amount = expense.expense_amount
        category_totals[category_name] = category_totals.get(category_name, 0) + amount
    categories = list(category_totals.keys())
    amounts = list(category_totals.values())

    plt.figure(figsize=(8, 6))
    plt.pie(amounts, labels=categories, autopct='%1.1f%%', startangle=140)
    plt.title('Expense Categories Distribution')
    plt.axis('equal') # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.show()

# Main function to generate user expense summary report
def generate_expense_summary_report(username, session):
    expenses = fetch_user_expenses(username, session)
    if expenses:
        total_spent = calculate_total_spent(expenses)
        print(f"Total amount spent by {username}: ${total_spent:.2f}")
        generate_category_pie_chart(expenses)
    else:
        print("No expenses found for the user.")

if __name__ == "__main__":
    username = input("Enter your username: ")
    generate_expense_summary_report(username)
