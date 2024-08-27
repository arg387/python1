""" import random
def fortune():
  random_fortune = random.randint(0,7)
  if random_fortune == 0:
    print("Don't pursue happiness – create it.")
  elif random_fortune == 1:
    print("All things are difficult before they are easy.")
  elif random_fortune == 2:
    print("The early bird gets the worm, but the second mouse gets the cheese.")
  elif random_fortune == 3:
    print("Someone in your life needs a letter from you.")
  elif random_fortune == 4:
    print("Don't just think. Act!")
  elif random_fortune == 5:
    print("Your heart will skip a beat.")
  elif random_fortune == 6:
    print("The fortune you search for is in another cookie.")
  else:
    print("Help! I'm being held prisoner in a Chinese bakery!")
fortune()
fortune()
fortune() """
# alternative code using list
import random
options = [
  'Don’t pursue happiness – create it.',
  'All things are difficult before they are easy.',
  'The early bird gets the worm, but the second mouse gets the cheese.',
  'If you eat something and nobody sees you eat it, it has no calories.',
  'Someone in your life needs a letter from you.',
  'Don’t just think. Act!',
  'Your heart will skip a beat.',
  'The fortune you search for is in another cookie.',
  'Help! I’m being held prisoner in a Chinese bakery!'
]

def fortune():
  random_fortune = random.randint(0, len(options) - 1)
  print(options[random_fortune])
# here whatever number we get from random fortune will be  called back with function call
fortune()
fortune()
fortune()