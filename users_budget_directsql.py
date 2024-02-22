import sqlite3


def add_user_and_budget(cursor, connection):
    print("Welcome to ExpendiTracker.")
    username = input("Enter your username: ")

    # Store user details
    try:
        cursor.execute("INSERT INTO Users (username) VALUES (?)", (username,))
        connection.commit()
        print(f"User {username} has been added successfully!")
    except sqlite3.Error as e:
        print("Error occured while adding user:", e)

    # Prompt user for their budget details
    budget_category = input("Enter the budget category: ")
    budget_amount = float(input(f"Enter the amount budgeted for {budget_category}: "))
    start_date = input("Enter the start date (YYYY-MM-DD): ")
    end_date = input("Enter the end date (YYYY-MM-DD): ")

    # Insert budget details into Budgets table
    try:
        cursor.execute("INSERT INTO Budgets (user_id, category_id, budget_amount, start_date, end_date) VALUES ((SELECT user_id FROM Users WHERE username = ?), (SELECT category_id FROM Categories WHERE category_name = ?), ?, ?, ?)",
                       (username, budget_category, budget_amount, start_date, end_date))
        connection.commit()
        print("Budget added successfully!")
    except sqlite3.Error as e:
        print("Error occurred while adding budget:", e)
    
    return username