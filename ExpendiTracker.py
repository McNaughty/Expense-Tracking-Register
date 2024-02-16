# Main Python file

from Expenses import Expense

import sqlite3

CONN = sqlite3.connect('./ExpendiTracker.db')
CURSOR = CONN.cursor()

def main():
    print(f"Running expense tracker")
    pass

    # register user and budget
    add_user_and_budget()

    # input expense
    expenses = get_expense()
    print(expenses)

    # save expenses in db
    store_expense(expenses)

    # read and summarise expenses
    summarise_expense()

def add_user_and_budget():
    print("Welcome to ExpendiTracker.")
    username = input("Enter your username: ")

    # Store user details
    try:
        CURSOR.execute("INSERT INTO Users (username) VALUES (?)", (username,))
        CONN.commit()
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
        CURSOR.execute("INSERT INTO Budgets (user_id, category_id, budget_amount, start_date, end_date) VALUES ((SELECT user_id FROM Users WHERE username = ?), (SELECT category_id FROM Categories WHERE category_name = ?), ?, ?, ?)",
                       (username, budget_category, budget_amount, start_date, end_date))
        CONN.commit()
        print("Budget added successfully!")
    except sqlite3.Error as e:
        print("Error occurred while adding budget:", e)

def get_expense():
    expense_name = input("Enter the name of the expense: ")
    expense_amount = float(input("Enter the amount of the expense: "))
    expense_category = input(f"Enter a category name:  ")
    new_expense = Expense(name=expense_name, category=expense_category, amount=expense_amount)
    return new_expense

    # expense_categories = [
        #     "Food", "House Shopping", "Enterntainment", "Work", "Black Tax"
        # ]


    # while True:
    #     print("Select the expense category: ")
    #     for i, category_name in enumerate(expense_categories):
    #         print(f" {i + 1}. {category_name}")

    #         # range selection for the users to know the number of options

    #     range_selection = f"[1 - {len(expense_categories)}]"

    #     index_selected = int(input(f"Enter a category number {range_selection}:  ")) - 1

    #     if index_selected in range(len(expense_categories)):
    #         selected_category = expense_categories[index_selected]

    #         # New expense created as an instance of the Expense class
    #         new_expense = Expense(name=expense_name, category=selected_category, amount=expense_amount)
    #         return new_expense
    #     else:
    #         print("Category does not exist, kindly try again!")

    #     break



def store_expense(expenses):
    print("Saving the expense...")
    try:
        # execute command for inserting into the expense table
        CURSOR.execute("INSERT INTO Expenses (expense_name, expense_amount, cat_id) VALUES (?, ?, ?)",
                       (expenses.name, expenses.amount, get_category_id(expenses.category)))
        CONN.commit()
        print("Expenses saved successfully!")
    except sqlite3.Error as e:
        print("Error occured while saving the expense:", e)



def get_category_id(category_name):
    try:
        #  FEtch category id from given name
         CURSOR.execute("SELECT category_id FROM Categories WHERE category_name = ?", (category_name,))
         category_id = CURSOR.fetchone()
         if category_id:
             return category_id[0]
         else:
             print("Category not found in the database.")
             return None 
           
    except sqlite3.Error as e:
        print("ERror occured while fetching category ID:", e)
    return None


   




def summarise_expense():
    print("Summarizing the expenses")


if __name__ == '__main__':
    main()