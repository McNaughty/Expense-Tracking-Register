import sqlite3

from Expenses import Expense


# CONN = sqlite3.connect('./ExpendiTracker.db')
# CURSOR = CONN.cursor()


def get_expense(currentuser):
    expense_name = input(f"{currentuser}, enter the name of the expense: ")
    expense_amount = float(input("Enter the amount of the expense: "))
    expense_category = input(f"Enter a category name:  ")
    new_expense = Expense(name=expense_name, category=expense_category, amount=expense_amount, expenseuser = currentuser)
    return new_expense




def store_expense(expenses, cursor, connection):
    print("Saving the expense...")
    try:
        # execute command for inserting into the expense table
        cursor.execute("INSERT INTO Expenses (expense_name, expense_amount, cat_id, userid) VALUES (?, ?, ?, (SELECT user_id FROM Users WHERE username = ?))",
                       (expenses.name, expenses.amount, get_category_id(expenses.category,cursor, connection), expenses.expenseuser))
        connection.commit()
        print("Expenses saved successfully!")
    except sqlite3.Error as e:
        print("Error occured while saving the expense:", e)



def get_category_id(category_name, cursor, connection):
    try:
        #  FEtch category id from given name
         cursor.execute("SELECT category_id FROM Categories WHERE category_name = ?", (category_name,))
         category_id = cursor.fetchone()
         if category_id:
             return category_id[0]
         else:
             print("Category not found in the database.")
             return None 
           
    except sqlite3.Error as e:
        print("Error occured while fetching category ID:", e)
    return None


   


