class Account:

    def __init__(self, balance, account_no):
        self.balance = balance
        self.account_no = account_no

    def debit(self, amount):
        if amount <= 0:
            print("Amount must be greater than zero.")
            return
        print(f"An amount of {amount} is debited")
        self.balance -= amount
        print(f"The available balance is {self.balance}")

    def credit(self, amount):
        if amount <= 0:
            print("Amount must be greater than zero.")
            return
        print(f"An amount of {amount} is credited")
        self.balance += amount
        print(f"The available balance is {self.balance}")

    def view_balance(self):
        print(f"The available balance is {self.balance}")


obj1 = Account(2000, "Abc1212")

print(f"\nWelcome to Your Bank Account: {obj1.account_no}")

while True:
    print("\n\nEnter 1 to deposit")
    print("Enter 2 to withdraw")
    print("Enter 3 to view balance")
    print("Enter 4 to exit")
    try:
        ch = int(input("Enter your choice:"))
    except:
        print("Enter numbers")
        continue

    if(ch == 1):
        amt = int(input("Enter the amount to deposit: "))
        obj1.credit(amt)
      
    elif(ch == 2):
        if obj1.balance <= 0:
            print("The available balance is 0.0 ")
            continue
        amt = int(input("Enter the amount to withdraw: "))
        if amt > obj1.balance:
            print("You have entered amount greater than the balance\nCheck balance and 'Try again' ")
            continue
        obj1.debit(amt)

    elif(ch == 3):
        obj1.view_balance()

    elif(ch == 4):
        print("You are exiting...")
        break

    else:
        print("Invalid choice. Try again.")
