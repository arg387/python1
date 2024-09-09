from random import sample
famous_houses = [  
  '🐺 Stark',
  '🐉 Targaryen',
  '🦌 Baratheon',
  '🦑 Greyjoy',
  '🦁 Lannister'
  ]
# using sample to get random items from the list [The number represent the number of random items will be shown in the output.]
# Check this for understanding sample method
#Since the .sample() method was directly imported, we can just write sample() instead of the usual random.sample().
example = sample(famous_houses,4)

print(f'Example:{example}')
# .choice() method returns one random item from the given list 
from random import choice
Ran = ["natural","shadow","negative","across","traffic","mistake"]
print(f"✅✅✅{choice(Ran)}")


# another code
from math import pi
from random import choice as ch
planets = [
  'Mercury',
  'Venus',
  'Earth',
  'Mars',
  'Saturn'
]
random_planet = ch(planets)
print(random_planet)
r = 0

if random_planet == 'Earth':
  r += 6371
  area = 4*pi*r*r
  print(f'The area of Earth is {round(area,2)}')
elif random_planet == 'Venus':
  r += 6052
  area = 4*pi*r*r
  print(f'The area of Venus is {round(area,2)}')
elif random_planet == 'Mercury':
  r += 2440
  area = 4*pi*r*r
  print(f'The area of Mercury is {round(area,2)}')
elif random_planet == 'Saturn':
  r += 58232
  area = 4*pi*r*r
  print(f'The area of Saturn is {round(area,2)}')
elif random_planet == 'Mars':
  r += 3390
  area = 4*pi*r*r
  print(f'The area of Mars is {round(area,2)}')
else:
  print('Oops! An error occurred.')