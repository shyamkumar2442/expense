class Expense:
    def __init__(self, date, category, amount, description):
        self.date = date
        self.category = category
        self.amount = amount
        self.description = description

    def __str__(self):
        return f"{self.date} | {self.category} | {self.amount} | {self.description}"

def add_expense(expenses):
    date = input("Enter the date : ")
    category = input("Enter the category: ")
    
    while True:
        try:
            amount = float(input("Enter the amount: "))
            break
        except ValueError:
            print("Please enter a valid number for the amount.")
    
    description = input("Enter a description for the category:")
    expenses.append(Expense(date, category, amount, description))
    print("Expense added successfully!")

def view_expenses(expenses):
    if not expenses:
        print("No expenses found.")
    else:
        print("Date | Category | Amount | Description")
        for expense in expenses:
            print(expense)

def write_expenses_to_file(expenses, filename):
    with open(filename, "w") as file:
        file.write("Date | Category | Amount | Description\n")
        for expense in expenses:
            file.write(f"{expense.date} | {expense.category} | {expense.amount} | {expense.description}\n")
   
    print("Expenses written to file successfully!")
   

def main():
    expenses = []
    filename = "expenses.txt"

    while True:
        print("\nExpense Tracker")
        print("1. Add expense")
        print("2. View expenses")
        print("3. Write expenses to file")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            write_expenses_to_file(expenses, filename)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

main()