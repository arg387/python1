try:
  integer = int(input("Please enter a number:"))
  print(1/integer)

except ValueError:
  print("You need to enter a number.")
except ZeroDivisionError:
  print("You can't enter zero.")
except Exception:
  print("Enter some valid number.")
finally:
  print("Thank you.")