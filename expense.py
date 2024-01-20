class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, amount, category, description):
        expense = {'amount': amount, 'category': category, 'description': description}
        self.expenses.append(expense)
        print("Expense added successfully.")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded.")
        else:
            print("Expense History:")
            for expense in self.expenses:
                print(f"Amount: ${expense['amount']}, Category: {expense['category']}, Description: {expense['description']}")

    def view_spending_patterns(self):
        if not self.expenses:
            print("No expenses recorded.")
        else:
            categories = set(expense['category'] for expense in self.expenses)
            print("Spending Patterns:")
            for category in categories:
                total_spent = sum(expense['amount'] for expense in self.expenses if expense['category'] == category)
                print(f"{category}: ${total_spent}")


def main():
    expense_tracker = ExpenseTracker()

    while True:
        print("\n1. Add Expense\n2. View Expenses\n3. View Spending Patterns\n4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            amount = float(input("Enter the expense amount: "))
            category = input("Enter the expense category: ")
            description = input("Enter a brief description: ")
            expense_tracker.add_expense(amount, category, description)
        elif choice == "2":
            expense_tracker.view_expenses()
        elif choice == "3":
            expense_tracker.view_spending_patterns()
        elif choice == "4":
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
