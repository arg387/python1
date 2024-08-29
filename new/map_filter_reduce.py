def bar(x):
  return x * x * x
lis = [8,10,9,7,6,5,4,3,2,1]
print((map(bar,lis))) #Output: <map object at 0x00000228CE70BB20>
l = list(map(bar,lis))
print(l)
