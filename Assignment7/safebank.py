class Account:
    ID = 1
    def __init__(self, initial_deposit):
        self.balance = initial_deposit
    def withdraw(self, amount):
            if self.locked_out == True:
                print("This account is locked. Please call.")
            else:
                if amount > self.balance:
                    return 0
                else:
                    self.balance -= amount
                    return amount
    def deposit(self, amount):
        if self.locked_out == True:
            print("This account is locked. Please call.")
        else:
            self.balance += amount
            return self
    def current_balance(self):
        return self.balance
                    
class Bank(Account):
    def __init__(self,name,initial_deposit):
        self.name = name
        Account.__init__(self,initial_deposit)
        self.ID = Account.ID
        Account.ID += 1
        self.locked_out = False
        self.numberwrong = 0
   
    def __str__(self):
        return "Name: {0} ID: {1} Balance: {2}".format(self.name, self.ID,self.current_balance())
                            
    def get_balance(self):
        while self.locked_out == False:
            self.idnumber = input("What is your id? ")
            if self.idnumber == str(self.ID):
                print(self)
                self.numberwrong = 0
            else:
                if self.numberwrong < 3:
                    self.numberwrong +=1
                    print("Please Try Again.")
                else:
                    print("This account is locked. Please call.")
                    self.locked_out = True
        
            
                                    
x1 = Bank("Kaiser", 100)
x2 = Bank("Ursala", 200)
x3 = Bank("Shilah", 75)
x1.get_balance()