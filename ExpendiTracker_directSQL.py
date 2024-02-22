# Main Python file

import sqlite3
from user_budget import add_user_and_budget
from expense_management import get_expense, store_expense
from expense_summaries import fetch_user_expenses, calculate_total_spent, generate_category_pie_chart,generate_expense_summary_report

CONN = sqlite3.connect('./ExpendiTracker.db')
CURSOR = CONN.cursor()

def print_menu():
    print("Welcome to ExpendiTracker.")
    print("Please choose from one of the following:")
    print("1. Create a budget")
    print("2. Register expense")
    print("3. Print summary of all your expenses")

def main():
    print_menu()
    optionSelected = input(": ")

    if (optionSelected == "1"):
        currentuser = add_user_and_budget(CURSOR, CONN)

    elif (optionSelected == "2"):
        currentuser = input("Please sepecify your username: ")
        expenses = get_expense(currentuser)
        store_expense(expenses, CURSOR, CONN)  

    elif optionSelected == "3": 
        username = input("Please specify your username: ")
        expenses = fetch_user_expenses(username)
        if expenses:
            total_spent = calculate_total_spent(expenses)
            print(f"Total amount spent by {username}: ${total_spent:.2f}")
            generate_category_pie_chart(expenses)
        else:
            print("No expenses found for the user.")

if __name__ == '__main__':
    main()
