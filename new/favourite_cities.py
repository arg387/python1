class Student:
  def __init__(self, name, age, grade):
    self.name = name
    self.age = age
    self.grade = grade

ladybird = Student('Christine McPherson', 12, 4.0)

print(vars(ladybird))
#In this example, below code defines a `City` class with a constructor (`__init__`) that initializes instances with ‘name’ and ‘country’ like attributes.
class City:
  def __init__(self,name,country,population,landmarks):
    self.name = name
    self.country = country
    self.population = population
    self.landmarks = landmarks
# Creating an instance of the City class 
city1 = City("Kolkata","India",20000000,["Victoria Hall","Saltlake Stadium","Thakurbari"])
city2 = City("Singapore City","Singapore",5917600,["Merlion","Esplanade","Gardens by the Bay"])
print(vars(city1))
print(vars(city2))
# Accessing attributes 
print(city2.landmarks)