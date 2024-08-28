# Write code below 💖
class Student:
  def __init__(self,name,year,enrolled,gpa):
    self.name = name
    self.year = year
    self.enrolled = enrolled 
    self.gpa = gpa
  def display_info(self):
    print('The Student ' + self.name + '\'s  gpa is ' + str(self.gpa) + '!')
  def graduation(self):
    if self.enrolled == True and self.gpa > 2.5 and self.year == 12:
      print(self.name + ' will be able to graduate this year.')
Saikat = Student("Saikat Khan", 12 , True, 3.0)
Sumon = Student("Sumon Biswas", 11 , True, 3.4)
Darcy = Student("Darcy Stuart", 8  , True, 3.1)
Saikat.display_info()
Sumon.display_info()
Darcy.display_info()
Saikat.graduation()
Sumon.graduation()
Darcy.graduation()

# Another example
class BankAccount:
  def __init__(self,first_name,last_name,account_id,account_type,pin,balance):
    self.first_name  = first_name
    self.last_name = last_name
    self.account_id = account_id
    self.account_type = account_type
    self.pin = pin
    self.balance = balance
  def deposit(self):
    type = int(input('Enter the pin:'))
    while type:
      if type == self.pin:
        amount = int(input("Enter the deposit amount : "))
        self.balance = self.balance + amount
        print(('name: ' + self.first_name + ' ' + self.last_name ) + '\naccount_id: ' + str(self.account_id) + '\naccount_type: '+ self.account_type)
        print('The current balance of ' + self.first_name +' '+self.last_name +' is ' + str(self.balance) + '$')
        break
      else:
        print('Wrong pin')
        type = int(input('Enter the pin:'))

  def withdraw(self):
    type = int(input('Enter the pin:'))
    
    while type:
      if type == self.pin:
        withdraw_amount = int(input("Enter the withdraw amount : "))
        self.balance = self.balance - withdraw_amount
        print(('name: ' + self.first_name + ' ' + self.last_name ) + '\naccount_id: ' + str(self.account_id) + '\naccount_type: '+ self.account_type)
        print('The current balance of ' + self.first_name +' '+self.last_name +' is ' + str(self.balance) + '$')
        break
      else:
        print('Wrong pin')
        type = int(input('Enter the pin:'))

  def display_balance(self):
    print(('name: ' + self.first_name + ' ' + self.last_name ) + '\naccount_id: ' + str(self.account_id) + '\naccount_type: '+ self.account_type + '\naccount_balance: '+ str(self.balance) + '$')
Customer1 = BankAccount('Surreal','Huge', 124334, 'ordinary', 1234,140)
Customer1.deposit()
Customer1.withdraw()
Customer1.display_balance()

# Alternative

class BankAccount1:
  def __init__(self, first_name, last_name, account_id, account_type, pin, balance):
    self.first_name = first_name
    self.last_name = last_name
    self.account_id = account_id
    self.account_type = account_type
    self.pin = pin
    self.balance = balance
  
  def deposit(self, amount):
    self.balance = self.balance + amount
    return self.balance

  def withdraw(self, amount):
    self.balance = self.balance - amount
    return self.balance

  def display_balance(self):
    print(f"${self.balance}")

checking_account = BankAccount1("Jane", "Doe", 13243546, "checking", 0000, 250.00)

checking_account.deposit(100)

checking_account.display_balance()

checking_account.withdraw(50)

checking_account.display_balance()