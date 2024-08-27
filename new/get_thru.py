def get_item(x):
  if x == 1:
    return '🍔 Cheeseburger'
  elif x == 2:
    return '🍟 Fries'
  elif x == 3:
    return '🥤 Soda'
  elif x == 4:
    return '🍦 Ice Cream'
  elif x == 5:
    return '🍪 Cookie'
  else:
    return 'Invalid value'
def welcome():
  print('Welcome dear customer\n Here\'s the menu:\n 1.🍔 Cheeseburger\n 2.🍟 Fries\n 3.🥤 Soda\n 4.🍦 Ice Cream\n 5.🍪 Cookie')
welcome()
option = int(input('What would you like to order? '))
print(get_item(option))