import random
my_numbers = []
winning_numbers = []
for i in range(0,5):  
  my_numbers.append(random.randint(1,69))
  winning_numbers.append(random.randint(1,69))

print(F"Before: {my_numbers}")
print(F"Before: {winning_numbers}")
my_numbers.append(random.randint(1,26))
winning_numbers.append(random.randint(1,26))
print(F"After: {my_numbers}")
print(F"After: {winning_numbers}")
