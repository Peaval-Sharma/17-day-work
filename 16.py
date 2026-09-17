class Bank:

    def __init__(self):
        self.balance = 0
        self.transactions = []

    def check_balance(self):
        print("Current Balance =", self.balance)

    def deposit(self):
        amount = float(input("Enter deposit amount: "))

        if amount > 0:
            self.balance += amount
            self.transactions.append("Deposited: " + str(amount))
            print("Amount deposited successfully.")
        else:
            print("Invalid amount.")

    def withdraw(self):
        amount = float(input("Enter withdrawal amount: "))

        if amount <= 0:
            print("Invalid amount.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            self.transactions.append("Withdrawn: " + str(amount))
            print("Amount withdrawn successfully.")

    def transaction_history(self):
        if len(self.transactions) == 0:
            print("No transactions found.")
        else:
            print("\nTransaction History:")
            for transaction in self.transactions:
                print(transaction)


bank = Bank()

while True:

    print("\n===== BANK ACCOUNT =====")
    print("1. Balance Inquiry")
    print("2. Deposit")
    print("3. Withdrawal")
    print("4. Transaction History")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        bank.check_balance()

    elif choice == 2:
        bank.deposit()

    elif choice == 3:
        bank.withdraw()

    elif choice == 4:
        bank.transaction_history()

    elif choice == 5:
        print("Thank you for using the bank.")
        break

    else:
        print("Invalid choice.")