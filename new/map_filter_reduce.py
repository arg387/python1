#MAP
def bar(x):
  return x * x * x
lis = [8,10,9,7,6,5,4,3,2,1]
print((map(bar,lis))) #Output: <map object at 0x00000228CE70BB20>
l = list(map(bar,lis))
print(l)

#FILTER
def filteration(a):
  return a>4
newll = list(filter(filteration,lis))
print(newll)
newll.sort() 
print(newll) #OUTPUT:[5, 6, 7, 8, 9, 10]

#REDUCE
from functools import reduce
def add(a,b):
  return a+b
sum = reduce(add,lis)
print(sum)#OUTPUT:16
print(reduce(lambda d,e:d+e,[1,2,3,4,5,6]))#OUTPUT:21
