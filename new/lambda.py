""" def appl(fx,value):
  return 6 +  fx(value)
cube = lambda x: x**3
print(appl(cube,4)) """
#short version
def appl(fx,value):
  return 6 +  fx(value)
print(appl(lambda x:x**3,4))
square = lambda x: x**2
print(square(3))
#example of multiple arguments
sum = lambda x,y,z: x + y + z
print(sum(1,2,3))
def add(x, y):
  answer = x + y
  return answer
total = add(4.99, 9.99)
print(total)