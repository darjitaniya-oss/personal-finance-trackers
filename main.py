from database import create_table
from finance import add_transaction, view_transactions

create_table()

while True:
    print("\n1 Add Income")
    print("2 Add Expense")
    print("3 View All")
    print("4 Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        amt = float(input("Enter income: "))
        add_transaction("income", amt)

    elif choice == "2":
        amt = float(input("Enter expense: "))
        add_transaction("expense", amt)

    elif choice == "3":
        view_transactions()

    elif choice == "4":
        break
