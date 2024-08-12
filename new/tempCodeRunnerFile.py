try:
  rating = float(input("Please give your review(0-5):"))

  if rating > 5 or rating < 0:
    print("Please type a value between 0 and 5.") 
  elif rating > 4.5:
    print('Extraordinary.')
  elif rating > 4:
    print('Excellent.')
  elif rating > 3:
    print('Good.')
  elif rating > 2:
    print('Fair.')
  else:
    print('Poor.')
except ValueError:
  print("Please type a number.")