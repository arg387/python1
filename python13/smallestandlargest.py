smallest = None
print("Before")
for value in [ 3 , 18 , 76 , 49 , 15 ] :
    if smallest is None :
        smallest = value
        # 'is' operater is similar to '==' but stronger than it in impression in python.
    elif smallest > value :
        smallest = value
    print ("smallest: ",smallest," value: ",value ) 
print("After", "smallest: ",smallest)
#1st type
largest = -1
print ("Before")
for value in [ 3 , 18 , 76 , 49 , 15 ] :
    if largest < value :
        largest = value
    print ("largest: ",largest," value: ",value )
print("After", "largest: ",largest) 
#2nd type
largest = None
print ("Before")
for value in [ 3 , 18 , 76 , 49 , 15 ] :
    if largest is None :
        largest = value
    elif largest < value :
        largest = value
    print ("largest: ",largest," value: ",value )
print("After", "largest: ",largest) 


