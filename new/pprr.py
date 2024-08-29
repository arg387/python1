def cube(x):
  return x * x * x

prl  = [1,2,3,4,5]
cube_l = []
for inp in prl:
  cube_l.append(cube(inp))
print(cube_l)