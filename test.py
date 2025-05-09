class MACHINE:
    def __init__(self):
        self.pin = ""
        self.balance = 12
        self.menu()  

    def menu(self):
        while True:
            print("\n--- MENU ---")
            print("1. Set/Change PIN")
            print("2. Check Balance")
            print("3. Withdraw Amount")
            print("4. Exit")

            choice = input("Select an option: ")

            if choice == "1":
                self.change_pin()
            elif choice == "2":
                if self.check_pin():
                    self.check_balance()
            elif choice == "3":
                if self.check_pin():
                    self.withdraw()
            elif choice == "4":
                print("Thank you for using the machine.")
                break
            else:
                print("Invalid option. Please try again.")

    def change_pin(self):
        if self.pin == "":
            print("No PIN set. Let's create one.")
        else:
            current = input("Enter current PIN: ")
            if current != self.pin:
                print("Incorrect PIN.")
                return

        new_pin = input("Enter new PIN: ")
        confirm = input("Confirm new PIN: ")
        if new_pin == confirm:
            self.pin = new_pin
            print("PIN changed successfully.")
        else:
            print("PINs do not match.")

    def check_pin(self):
        entered_pin = input("Enter your PIN: ")
        if entered_pin == self.pin:
            return True
        else:
            print("Incorrect PIN.")
            return False

    def check_balance(self):
        print(f"Your current balance is: ${self.balance}")

    def withdraw(self):
        try:
            amount = float(input("Enter amount to withdraw: "))
            if amount <= self.balance:
                self.balance -= amount
                print(f"${amount} withdrawn successfully.")
                print(f"Remaining balance: ${self.balance}")
            else:
                print("Insufficient funds.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


