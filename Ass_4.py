


import random


class Bank:
    def __init__(self):
        self.balance = 0

    def openAccount(self):
        self.name = input("Enter your name: ")
        self.db = input("Enter your date of birth: ")
        self.add = input("Enter your address: ")
        self.cn = input("Enter your contact number: ")
        self.Id = input("Enter your Aadhar number: ")
        self.PAN = input("Enter your PAN number: ")
        self.accn = random.randint(100000, 999999)
        print("Your account number: {self.accn}")

    def deposit(self):
        amount = float(input("Enter the amount to be deposited\n"))
        self.balance = self.balance + amount
        print("Amount Deposited:{amount}")

    def withdraw(self):
        amount = float(input("Enter the amount to be withdrawn\n"))
        if self.balance >= amount:
            self.balance -= amount
            print("Amount Withdrawn:", amount)
        else:
            print("Sorry, Insufficient Balance")

    def checkBalance(self):
        print("Your Acccount balance:", self.balance)

    def displayinfo(self):
        print("NAME: {self.name}")
        print("DOB: {self.db}")
        print("ADDRESS: {self.add}")
        print("CONTACT NUMBER: {self.cn}")
        print("ACCOUNT NUMBER: {self.accn}")


b1 = Bank()

print('''
        Welcome to the State Bank of India
        Main Menu
        1.OPEN NEW ACCOUNT
        2.DEPOSIT AMOUNT
        3.WITHDRAW AMOUNT
        4.BALANCE ENQUIRY
        5.DISPLAY CUSTOMER DETAILS
        6.EXIT ''')

while True:
    choice = int(input("Enter your choice:"))

    if choice == 1:
        b1.openAccount()

    elif choice == 2:
        b1.deposit()

    elif choice == 3:
        b1.withdraw()

    elif choice == 4:
        b1.checkBalance()

    elif choice == 5:
        b1.displayinfo()

    elif choice == 6:
        print("EXIT")
        break


    else:
        print("Invalid Input")