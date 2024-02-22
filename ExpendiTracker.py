from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from user_budget import add_user_and_budget
from expense_management import get_expense, store_expense
from expense_summaries import fetch_user_expenses, calculate_total_spent, generate_category_pie_chart, generate_expense_summary_report
from models import User, Expense  # Importing SQLAlchemy models

# Create SQLAlchemy engine and session
engine = create_engine('sqlite:///ExpendiTracker.db')  # Replace 'ExpendiTracker.db' with your actual database file
Session = sessionmaker(bind=engine)
session = Session()

def print_menu():
    print("Welcome to ExpendiTracker.")
    print("Please choose from one of the following:")
    print("1. Create a budget")
    print("2. Register expense")
    print("3. Print summary of all your expenses")

def main():
    print_menu()
    option_selected = input(": ")

    if option_selected == "1":
        current_user = add_user_and_budget(session)

    elif option_selected == "2":
        current_user = input("Please specify your username: ")
        expenses = get_expense(current_user, session)
        store_expense(expenses, session)

    elif option_selected == "3":
        username = input("Please specify your username: ")
        generate_expense_summary_report(username, session)

if __name__ == '__main__':
    main()
