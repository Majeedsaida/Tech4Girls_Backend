class BankAccount:
    # Class variable
    bank_name = "Tech4Girls Bank"

    def __init__(self, account_holder):
        # Instance variables
        self.account_holder = account_holder
        self.balance = 0

    def deposit(self, amount):
        """Add money to the account."""
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        """Deduct money, ensuring the balance doesn’t go negative."""
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

    @staticmethod
    def bank_policy():
        """Prints a generic bank policy message."""
        print("Bank policy: Maintain a minimum balance of $10.")

    @classmethod
    def get_bank_name(cls):
        """Return the bank's name."""
        return cls.bank_name


# Demonstrate usage
account = BankAccount("Alice")
print("Bank Name:", BankAccount.get_bank_name())
account.deposit(100)
account.withdraw(30)
account.withdraw(80)
BankAccount.bank_policy()
