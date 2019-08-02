import json
import os
import random 
import view

PATH = os.path.dirname(__file__)
DATA = "data.json"
DATAPATH = os.path.join(PATH,DATA)

data = {}

def load():
    global data
    with open(DATAPATH, "r") as accounts:
        data = json.load(accounts)


def save():
    with open(DATAPATH, "w") as accounts:
        json.dump(data, accounts, indent=2)

#save new account details into json

def new account(view.create_account):
    

#generate random account
def gen_account():
        for x in range(5):
                print(random.randint(0,9), end = '')

new_account = gen_account()

#add account

def add_account(new_account):
        data['accounts'][account]={viewmain.create_account()}

def login_verify():
        account_num = input("Account Number: ")
        pin_verify = input("PIN: ")
        for item in accounts:
            if account_num in accounts and accounts[account_num] == pin_verify:
                print('Login Successful')
        else:
                print("Login failed")


class Bankaccount:
    def __init__(self,id,pin,balance=0):
        self.id = id
        self.pin = pin
        self.balance = balance

    def getId(self):
        return self.id
 
    def getBalance(self):
        return self.balance
 
    def withdraw(self, amount):
        if self.balance - amount > 0:
                self.balance -= amount
        else:
                viewsecondary.insuff_funds()
 
    def deposit(self, amount):
        self.balance += amount