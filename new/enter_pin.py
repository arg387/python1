print("--------------------------------- \n WELCOME TO BANK OF INDIA. \n --------------------------------")
pin = int(input("Enter your pin:"))
while pin != 1234:
  pin = int(input("INCORRECT PIN. Enter your pin again:"))
if pin == 1234:
  print("CONGRATS! PIN IS CORRECT...")