from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, Budget, Category  # Importing SQLAlchemy models

def add_user_and_budget(session):
    print("Welcome to ExpendiTracker.")
    username = input("Enter your username: ")

    try:
        # Create a new User instance and add it to the session
        new_user = User(username=username)
        session.add(new_user)
        session.commit()
        print(f"User {username} has been added successfully!")
    except Exception as e:
        print("Error occurred while adding user:", e)

    # Prompt user for their budget details
    budget_category = input("Enter the budget category: ")
    budget_amount = float(input(f"Enter the amount budgeted for {budget_category}: "))
    start_date = input("Enter the start date (YYYY-MM-DD): ")
    end_date = input("Enter the end date (YYYY-MM-DD): ")



    try:
        # Convert date strings to Python date objects
        start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
        end_date = datetime.strptime(end_date, '%Y-%m-%d').date()

        # Query the category from the database
        category = session.query(Category).filter(Category.category_name == budget_category).first()

        # Create a new Budget instance and add it to the session
        new_budget = Budget(user=new_user, category=category, budget_amount=budget_amount, start_date=start_date, end_date=end_date)
        session.add(new_budget)
        session.commit()
        print("Budget added successfully!")
    except Exception as e:
        print("Error occurred while adding budget:", e)
    
    return username

if __name__ == "__main__":
    # Create SQLAlchemy engine and session
    engine = create_engine('sqlite://db/ExpendiTracker.db')  
    Session = sessionmaker(bind=engine)
    session = Session()

    # Call the function to add user and budget
    add_user_and_budget(session)
