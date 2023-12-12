class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"${amount:.2f} deposited successfully."
        else:
            return "Invalid deposit amount."

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"${amount:.2f} withdrawn successfully."
        else:
            return "Insufficient funds or invalid withdrawal amount."

    def check_balance(self):
        return f"Current Balance: ${self.balance:.2f}"

# Example Usage
if __name__ == "__main__":
    account_holder_name = input("Enter account holder's name: ")
    initial_balance = float(input("Enter initial balance (press Enter for default 0): ") or 0)

    account = BankAccount(account_holder_name, initial_balance)

    while True:
        print("\nBank Account Menu:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            deposit_amount = float(input("Enter deposit amount: "))
            print(account.deposit(deposit_amount))
        elif choice == '2':
            withdrawal_amount = float(input("Enter withdrawal amount: "))
            print(account.withdraw(withdrawal_amount))
        elif choice == '3':
            print(account.check_balance())
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")