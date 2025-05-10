from new import Atm, UserAtm  

def main():
    user1 = UserAtm("Aaryan Karki")
    user1.greet_user()
    user1.set_pin("1234")
    user1.balance = 500
    user1.check_balance()
    user1.withdraw(200)

if __name__ == "__main__":
    main()
