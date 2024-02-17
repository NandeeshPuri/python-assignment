import sqlite3
from datetime import datetime

class ExpenseTracker:
    def __init__(self, db_name="expense_tracker.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS expenses (
                            id INTEGER PRIMARY KEY,
                            amount REAL,
                            category TEXT,
                            date TEXT
                            )''')
        self.conn.commit()

    def add_expense(self, amount, category):
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor = self.conn.cursor()
        cursor.execute('''INSERT INTO expenses (amount, category, date) VALUES (?, ?, ?)''',
                       (amount, category, date))
        self.conn.commit()

    def view_expenses(self):
        cursor = self.conn.cursor()
        cursor.execute('''SELECT * FROM expenses ORDER BY date DESC''')
        expenses = cursor.fetchall()
        for expense in expenses:
            print(f"ID: {expense[0]}, Amount: {expense[1]}, Category: {expense[2]}, Date: {expense[3]}")

    def view_spending_patterns(self):
        cursor = self.conn.cursor()
        cursor.execute('''SELECT category, SUM(amount) FROM expenses GROUP BY category''')
        spending_patterns = cursor.fetchall()
        for pattern in spending_patterns:
            print(f"Category: {pattern[0]}, Total Amount: {pattern[1]}")

def main():
    expense_tracker = ExpenseTracker()

    while True:
        print("\n1. Add Expense")
        print("2. View Expenses")
        print("3. View Spending Patterns")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            expense_tracker.add_expense(amount, category)
            print("Expense added successfully.")
        elif choice == "2":
            print("\n--- All Expenses ---")
            expense_tracker.view_expenses()
        elif choice == "3":
            print("\n--- Spending Patterns ---")
            expense_tracker.view_spending_patterns()
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
