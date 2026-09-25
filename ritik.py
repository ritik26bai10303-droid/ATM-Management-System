# User Account Balance And pin
balance = 10000
pin = "1234"
transactions = []# empty transaction list 

# to check balance of the user
def check_balance(balance):
    print("\nYour current balance is: ₹", balance)

# user will ask to withdraw money from account
def withdraw_money(balance):
    entered_pin = input("Enter your PIN to withdraw cash: ")

    if entered_pin != pin:
        print("Incorrect PIN.")
        return balance

    amount = float(input("Enter amount to withdraw: ₹"))

    if amount <= 0:
        print("Amount must be greater than 0.")
        return balance

    if amount > balance:
        print("Insufficient balance.")
        return balance

    balance = balance - amount
    transactions.append("Withdrawn: ₹" + str(amount))

    print("Please collect your cash.")
    print("Remaining balance: ₹", balance)

    return balance

# If user want to deposit money to account
def deposit_money(balance):
    amount = float(input("Enter amount to deposit: ₹"))

    if amount <= 0:
        print("Amount must be greater than 0.")
        return balance

    balance = balance + amount
    transactions.append("Deposited: ₹" + str(amount))

    print("Amount deposited successfully.")
    print("Updated balance: ₹", balance)

    return balance

# user can check his transaction history 
def transaction_history():
    print("\n===== TRANSACTION HISTORY =====")

    if len(transactions) == 0:
        print("No transactions found.")
    else:
        for transaction in transactions:
            print(transaction)

# Main Page that will shown to user at time of login
print("===== WELCOME TO ATM =====")

while True:
    print("\n===== ATM MENU =====")
    print("1. Check Balance")
    print("2. Withdraw Money")
    print("3. Deposit Money")
    print("4. Transaction History")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        check_balance(balance)

    elif choice == "2":
        balance = withdraw_money(balance)

    elif choice == "3":
        balance = deposit_money(balance)

    elif choice == "4":
        transaction_history()

    elif choice == "5":
        print("Thank you for using the ATM.")
        break

    else:
        print("Invalid choice. Please try again.")
