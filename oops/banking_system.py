class Bank:
    bankname = "State Bank of India"

    def __init__(self,name, balance=0.0):
        self.name = name
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount

    def withdraw(self,amount):
        if amount > self.balance:
            print("insufficient balance")
        else:
            self.balance = self.balance - amount 

    def show_balance(self):
        print("your total balance is ", self.balance)


c1 = Bank("Ashish")
while True:
    cmd = input("enter d for deposit \n w for withdraw \n t for total balance \n e for exit")

    if cmd == "d":
        amount = int(input("enter the amount to deposit "))
        c1.deposit(amount)
    elif cmd == "w":
        amount = int(input("enter amount to withdraw"))
        c1.withdraw(amount)
    elif cmd == "t":
        c1.show_balance()
    else : 
        print("thank for the banking ")
        break
