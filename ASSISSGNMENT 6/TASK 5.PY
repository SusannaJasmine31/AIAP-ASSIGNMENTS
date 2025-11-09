class BankAccount:
    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 1000   # Fixed starting balance

    def deposit(self):
        print("Deposited: 500")
        self.balance += 500   # Fixed deposit amount

    def withdraw(self):
        print("Withdrawn: 300")
        self.balance -= 300   # Fixed withdrawal amount

    def show_details(self):
        print("Account Holder Name:", self.account_holder)
        print("Current Balance:", self.balance)


# Taking only the name from user
name = input("Enter Account Holder Name: ")

# Creating object
account = BankAccount(name)

# Performing fixed operations
account.show_details()
account.deposit()
account.withdraw()
account.show_details()