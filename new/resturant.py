

class Student:
  student_id = 0
  name = ''
  year = 0
  gpa = 0.0
  enrolled = False
ferris = Student() # instance of class student
ferris.name = 'Ferris Butler'
ferris.student_id = 1
ferris.year = 6
ferris.gpa = 3.8
ferris.enrolled = True
# You can check all the attributes available on the ferris object with the built-in vars() function
print(vars(ferris))
# Output: {'student_id': 10837, 'name': 'Ferris Bueller', 'year': 12, 'gpa': 3.81, 'enrolled': True} 
# This will print out all the attributes of the object in the form of dictionary
# Method is the function that is part of a class
# Python instance : Subbranches of the python class if the class is your character type then the instance is the your character or if your class is the car then your instance will be a specified car
# Python class : The blueprint of the python object or the python character or the python car
# Python class variable : The variable that is defined inside the class and is shared by all the instances
# Python instance variable : The variable that is defined inside the class and is unique to each instance
# Attributes are the defining characteristics of our class
""" class car:
  pass """ # tells python that this class will be empty.

class Restaurant:
  name = ""
  category = ""
  rating = 0.0
  delivery = False

bobs_burgers = Restaurant()
bobs_burgers.name = 'Bob\'s Burgers'
bobs_burgers.category = 'American Diner'
bobs_burgers.rating = 4.7
bobs_burgers.delivery = False

print(vars(bobs_burgers))