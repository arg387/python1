x = 5
if x < 10:
    print("Small")
if x > 20:
    print("Large")
    # make sure to take care of indent / spacing. python is sensitive on it.
if x == 5:
    print("Is 5")
    print("Is still 5")
    
print("Afterwards 5")

if x == 6:
    print("Is 6")
    print("Is still 6")
print("Afterwards 6")
# if conditions are true then codelines will be executed or else ignored.
# And so this indenting is a way to, in effect, make bigger blocks of conditional code, or multi-line blocks of conditional code.
print("Finish")

y = 7
if y == 5:
    print("True")
    
else:
    print("False")
print("done")
# if - else statement example
z = 20
if z < 5:
    print("Small")
elif z < 10:
    print("Medium")
else:
    print("Large")

