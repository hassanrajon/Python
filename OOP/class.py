class Atm:
    def __init__(self):
        self.pin=""
        self.balance=0
        self.menu()
    def menu(self):
        user_input = input("""
                           please enter how you wat to proceed:
                           1- set pin
                           2- Deposit
                           3- Withdraw
                           4- check balance
                           5- exit    
                           """)  
        if user_input=="1":
            self.set_pin()
        elif user_input=="2":
            self.deposit()
        elif user_input=="3":
            self.withdraw()
        elif user_input=="4":
            self.check_balance()
        else: 
          pass                
    def set_pin(self):
        self.pin=input("please enter your pin: ")
        print("pin set up successful")
    def deposit(self):
         user_input=input("please enter your pin: ")
         if(user_input==self.pin):
             amount=int(input("please enter amount: "))
             self.balance+=amount; 
             print("Deposit successful")
         else:
             print("invalid pin")        
    def withdraw(self):
         user_input=input("please enter your pin: ")
         if(user_input==self.pin):
             amount=int(input("please enter amount: "))
             self.balance-=amount; 
             print("Withdraw successful")
         else:
             print("invalid pin")   
    def check_balance(self):
         user_input=input("please enter your pin: ")
         if(user_input==self.pin):
             print("your balance is "+self.balance)
         else:
             print("invalid pin")   
                       
dbbl = Atm()              