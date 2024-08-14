import random
dice1 = random.randint(1,6)
dice2 = random.randint(1,6)
total = dice1 + dice2
guess = int(input('What is the total?'))
while total != guess:
  guess = int(input('What is the total?'))

print('You got it!')

