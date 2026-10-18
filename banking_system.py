
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Amount deposited successfully.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print("Amount withdrawn successfully.")
        else:
            print("Insufficient balance or invalid amount.")

    def get_balance(self):
        return self.__balance

    def display(self):
        print("Account Holder:", self.account_holder)
        print("Balance:", self.__balance)


class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance, interest_rate):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def deposit(self, amount):
        super().deposit(amount)
        print("Savings account deposit completed.")

    def display(self):
        super().display()
        print("Interest Rate:", self.interest_rate, "%")


class CurrentAccount(BankAccount):
    def __init__(self, account_holder, balance, overdraft_limit):
        super().__init__(account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if 0 < amount <= self.get_balance() + self.overdraft_limit:
            super().withdraw(min(amount, self.get_balance()))
            extra = amount - min(amount, self.get_balance())
            if extra > 0:
                print("Overdraft used:", extra)
                print("Overdraft is a simulated limit; balance remains unchanged below zero.")
        else:
            print("Overdraft limit exceeded.")

    def display(self):
        super().display()
        print("Overdraft Limit:", self.overdraft_limit)


print("----- Banking System -----")
name = input("Enter account holder name: ")
balance = float(input("Enter initial balance: "))

print("\nChoose Account Type")
print("1. Savings Account")
print("2. Current Account")
choice = int(input("Enter your choice: "))

if choice == 1:
    rate = float(input("Enter interest rate (%): "))
    account = SavingsAccount(name, balance, rate)
elif choice == 2:
    limit = float(input("Enter overdraft limit: "))
    account = CurrentAccount(name, balance, limit)
else:
    print("Invalid account type.")
    exit()

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Display Account Details")
    print("5. Exit")

    option = int(input("Enter your choice: "))

    if option == 1:
        amount = float(input("Enter deposit amount: "))
        account.deposit(amount)

    elif option == 2:
        amount = float(input("Enter withdrawal amount: "))
        account.withdraw(amount)

    elif option == 3:
        print("Current Balance:", account.get_balance())

    elif option == 4:
        account.display()

    elif option == 5:
        print("Thank you for using the Banking System.")
        break

    else:
        print("Invalid choice. Try again.")
