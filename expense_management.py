from sqlalchemy import engine_from_config
from models import Expense, User, Category  # Importing SQLAlchemy models
from sqlalchemy.orm import sessionmaker

# Create SQLAlchemy session
Session = sessionmaker(bind=engine_from_config)
session = Session()

def get_expense(currentuser, session):
    expense_name = input(f"{currentuser}, enter the name of the expense: ")
    expense_amount = float(input("Enter the amount of the expense: "))
    expense_category = input(f"Enter a category name:  ")

    # Retrieve the User instance corresponding to the provided currentuser
    user = session.query(User).filter(User.username == currentuser).first()
    if not user:
        print(f"User '{currentuser}' not found.")
        return None

    # Retrieve the Category instance corresponding to the provided category name
    category = session.query(Category).filter(Category.category_name == expense_category).first()
    if not category:
        print(f"Category '{expense_category}' not found.")
        return None

    # Create a new Expense instance with the retrieved User and Category instances
    new_expense = Expense(expense_name=expense_name, expense_amount=expense_amount, category=category, user=user)
    return new_expense


def store_expense(expense, session):
    if expense is None:
        print("Expense object is None. Cannot save.")
        return

    print("Saving the expense...")
    try:
        session.add(expense)
        session.commit()
        print("Expense saved successfully!")
    except Exception as e:
        print("Error occurred while saving the expense:", e)


def get_category_id(category_name, session):
    try:
        category = session.query(Category).filter(Category.category_name == category_name).first()
        if category:
            return category.category_id
        else:
            print("Category not found in the database.")
            return None
    except Exception as e:
        print("Error occurred while fetching category ID:", e)
        return None

if __name__ == "__main__":
    currentuser = input("Enter your username: ")
    new_expense = get_expense(currentuser)
    store_expense(new_expense, session)
