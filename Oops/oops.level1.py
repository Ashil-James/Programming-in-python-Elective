class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        
    def showBalance(self):
        return f"{self.owner}'s balance: ₹{self.balance}"  # return
        
    def deposit(self, amount):
        self.balance += amount
        print(f"₹{amount} was deposited")
        print(self.showBalance())   # now prints the returned string
        
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else: 
            self.balance -= amount
            print(f"Withdrew ₹{amount}.")
            print(self.showBalance())

acc = BankAccount("Ash", 5000)
print(acc.showBalance())
acc.deposit(1000)
acc.withdraw(2000)
acc.withdraw(9000)