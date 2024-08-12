for i in range(1,17):
  if i % 3 == 0 and i != 15:
    print("Fizz")
  elif i % 5 == 0 and i !=15:
    print("Buzz")
  elif i == 15:
    print("FizzBuzz")
  elif i == 16:
    print("...")
  else:
    print(i)

