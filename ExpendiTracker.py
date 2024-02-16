# Main Python file

import sqlite3
from user_budget import add_user_and_budget
from expense_management import get_expense, store_expense

CONN = sqlite3.connect('./ExpendiTracker.db')
CURSOR = CONN.cursor()

def main():
    print("Running expense tracker")
    currentuser = add_user_and_budget(CURSOR, CONN)
    expenses = get_expense(currentuser)
    store_expense(expenses, CURSOR, CONN)

if __name__ == '__main__':
    main()





def summarise_expense():
    print("Summarizing the expenses")


if __name__ == '__main__':
    main()