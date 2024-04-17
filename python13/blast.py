#conditional and loop statements
n = 5
while n > 0 :
    print(n)
# without break statement the code will become an infinite loop. since while always identify an infinite loop
    
    n = n - 1
print("Stop")

# because of break statement next line after break statement inside the indent is skipped.

nam = input ('Who are you?')
print( "Welcome", nam)

while True:
    line = input('> ')
    if  line[0] == '#' :
        continue
    if  line ==  'done' :
        break
    print(line)
print('Done!')