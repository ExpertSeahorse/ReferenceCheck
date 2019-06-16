class Account:
    """This class is used as a reference to remember how to build constructors and use classes"""
    '''def __init__(self):
        self.name = ""
        self.acctNum = 0
        self.balance = 0.0'''

    def __init__(self, n, a, b):
        self.name = n
        self.acctNum = a
        self.balance = b

    def displayAccount(self):
        print("Name: ", self.name, ", Account Number: ", self.acctNum, ", Balance: ", self.balance)


# Establishes accounts
acct1 = Account("Matt", 17503725, 20000.00)
acct2 = Account("Joe", 47595837, 13.87)
acct3 = Account("", 0, 0)

# Sets values for acct3
acct3.name = "Daniel"
acct3.acctNum = 9283475
acct3.balance = 400.67

# Prints Accounts manually
acct1.displayAccount()
print("Name: {}, Account Number: {}, Balance: {}".format(acct2.name, acct2.acctNum, acct2.balance))

# Prints Accounts Automatically
accounts = [acct1, acct2, acct3]
i=0
for i in range(i,len(accounts)):
    print("Name: {}, Account Number: {}, Balance: {}".format(accounts[i].name, accounts[i].acctNum, accounts[i].balance))
