Earth_Weight = float(input('What is your earth weight:'))
Planet = int(input('What is the planet number?:'))

if Planet == 1:
  print('destination weight = '+ str(Earth_Weight * 0.38))
elif Planet == 2:
  print('destination weight = '+ str(Earth_Weight * 0.91))
elif Planet == 3:
  print('destination weight = '+ str(Earth_Weight * 0.38))
elif Planet == 4:
  print('destination weight = '+ str(Earth_Weight * 2.53))
elif Planet == 5:
  print('destination weight = '+ str(Earth_Weight * 1.07))
elif Planet == 6:
  print('destination weight = '+ str(Earth_Weight * 0.89))
elif Planet == 7:
  print('destination weight = '+ str(Earth_Weight * 1.14))
else:
  print('Invalid planet number')
  #Alternative
""" 
earth_weight = float(input('What is your earth weight:'))
Planet = int(input('What is the planet number?:'))

if Planet == 1:
  destination_weight = earth_weight * 0.38
  print(destination_weight)
elif Planet == 2:
  destination_weight = earth_weight * 0.91
  print(destination_weight)
elif Planet == 3:
  destination_weight = earth_weight * 0.38
  print(destination_weight)
elif Planet == 4:
  destination_weight = earth_weight * 2.53
  print(destination_weight)
elif Planet == 5:
 destination_weight = earth_weight * 1.07
 print(destination_weight)
elif Planet == 6:
  destination_weight = earth_weight * 0.89
  print(destination_weight)
elif Planet == 7:
  destination_weight = earth_weight * 1.14
  print(destination_weight)
else:
  print('Invalid planet number')
 """