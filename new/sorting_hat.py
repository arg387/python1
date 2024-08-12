gryffindor = 0
hufflepuff = 0
ravenclaw = 0
slytherin = 0
print('===============')
print('The Sorting Hat')
print('===============')


print("Q1: When I’m dead, I want people to remember me as:-\n  1) The Good\n  2) The Great\n  3) The Wise\n  4) The Bold")
answer = int(input("Enter your Answer(1-4): "))

if answer == 1:
  gryffindor =+ 4
elif answer == 2:
  hufflepuff =+ 4
elif answer == 3:
  ravenclaw =+ 4 
elif answer == 4:
  slytherin =+ 4
else:
  print("Wrong INPUT...")
print("Q2: Which kind of instrument most pleases your ear?:-\n  1) The violin\n  2) The trumpet\n  3) The piano\n  4) The drum")
answer = int(input("Enter your Answer(1-4): "))

if answer == 1:
  ravenclaw =+ 2
elif answer == 2:
  gryffindor=+ 2
elif answer == 3:
  slytherin =+ 2 
elif answer == 4:
  hufflepuff =+ 2
else:
  print("Wrong INPUT...")
print("Q3: Do you like Dawn or Dusk?:-\n  1) Dawn\n  2) Dusk")
answer = int(input("Enter your Answer(1-2):"))

if answer == 1:
  gryffindor += 1
  ravenclaw += 1
elif answer == 2:
  hufflepuff += 1
  slytherin +=1
else:
  print('Wrong input.')

print("gryffindor:", gryffindor)
print("ravenclaw:" , ravenclaw)
print("hufflepuff:",  hufflepuff)
print("slytherin:" ,slytherin)

if gryffindor > ravenclaw and gryffindor > hufflepuff and gryffindor > slytherin:
  print(" 🦁 Gryffindor")
elif ravenclaw > hufflepuff and ravenclaw > slytherin:
  print(" 🦅 Ravenclaw")
elif hufflepuff > slytherin:
  print(" 🦡 Hufflepuff")
else:
  print(" 🐍 Slytherin")


