#1st technique
bill = [13.99, 28.75, 9.99, 9.99, 6.95, 7.45, 16.45, 16.45]
total = sum(bill)
newSum = total/4
perPerson = total/len(bill)
print(perPerson)
# -----------------------------------------------
#2nd technique
bill = [13.99, 28.75, 9.99, 9.99, 6.95, 7.45, 16.45, 16.45]
total = 0
for element in bill:
  total = total + element
my_share = total/len(bill)
print(total)
print(my_share)
