class Atm:
    def __init__(self):
        self.pin = ""
        self.balance = 0

    def set_pin(self, new_pin):
        self.pin = new_pin
        print("PIN set successfully.")

    def check_balance(self):
        print(f"Your balance is: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn {amount}. Remaining balance: {self.balance}")
        else:
            print("Insufficient balance.")


class UserAtm(Atm):
    def __init__(self, username):
        super().__init__()  # Call parent constructor
        self.username = username

    def greet_user(self):
        print(f"Welcome, {self.username}!")

  