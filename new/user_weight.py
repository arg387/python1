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
