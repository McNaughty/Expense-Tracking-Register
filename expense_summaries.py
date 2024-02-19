import sqlite3
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

CONN = sqlite3.connect('./ExpendiTracker.db')
CURSOR = CONN.cursor()

# Function to fetch user's expenses from the database
def fetch_user_expenses(username):
    try:
        CURSOR.execute("""
            SELECT e.*, c.category_name 
            FROM Expenses e 
            JOIN Categories c ON e.cat_id = c.category_id
            WHERE e.userid = (SELECT user_id FROM Users WHERE username = ?)
        """, (username,))
        expenses = CURSOR.fetchall()
        print(f"{expenses}")
        return expenses
    except sqlite3.Error as e:
        print("Error fetching user's expenses:", e)
        return None

# Function to calculate total amount spent by the user
def calculate_total_spent(expenses):
    total_spent = sum(expense[2] for expense in expenses)
    return total_spent

# Function to generate a pie chart of expenses by category
def generate_category_pie_chart(expenses):
    category_totals = {}
    for expense in expenses:
        category = expense[5]  
        amount = expense[2]
        category_totals[category] = category_totals.get(category, 0) + amount
    categories = list(category_totals.keys())
    amounts = list(category_totals.values())

    plt.figure(figsize=(8, 6))
    plt.pie(amounts, labels=categories, autopct='%1.1f%%', startangle=140)
    plt.title('Expense Categories Distribution')
    plt.axis('equal') # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.show()

# Main function to generate user expense summary report
def generate_expense_summary_report(username):
    expenses = fetch_user_expenses(username)
    if expenses:
        total_spent = calculate_total_spent(expenses)
        print(f"Total amount spent by {username}: ${total_spent:.2f}")
        generate_category_pie_chart(expenses)
    else:
        print("No expenses found for the user.")
