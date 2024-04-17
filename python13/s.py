# for multiple output
score = input("Enter Score: ")
scores = float(score)
if scores >= 0.9 :
    print("A")
elif scores >= 0.8 :
    print("B")
elif scores >= 0.7 :
    print("C")
elif scores >= 0.6 :
    print("D")
elif scores < 0.6 :
    print("F")  
# for one output 
score = input("Enter Score: ")
scores = float(score)
if scores >= 0.9 :
    print("A")
elif scores >= 0.8 :
    print("B")
elif scores >= 0.7 :
    print("C")
else:
    print("F")
# different way for one output
score = input("Enter Score: ")
scores = float(score)
if scores == 0.9 :
    print("A")
elif scores >= 0.8 :
    print("B")
elif scores >= 0.7 :
    print("C")
elif scores >= 0.6 :
    print("D")
elif scores < 0.6 :
    print("F")  