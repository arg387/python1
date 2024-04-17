i = 0.99
print(type(i))
a = int(i)
print(type(a))
print(a)
hrs = input("Enter Hours:")
hour = float(hrs)
rate = input("Enter rate:")
# here inputs are regarded as strings so conversion is needed
rates = float(rate)
pay = int(hour * rates)
# direct conversion of floats into integer
print("Pay:", pay)