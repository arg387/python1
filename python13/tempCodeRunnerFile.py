###
def computepay(h, r):
    if h >= 40:
        return 40 * r + (h - 40) * r * 1.5
    else:
        return h * r

def main():
    
    try: 
        int1 = input("Enter Hours")
        h = float(int1)
        int2= input("Enter Rate")
        r = float(int2)
    # only catch the expected errors
    except ():
        print ("Error, please enter a numeric input")
        quit()
    print(computepay(h,r))
main()



###
def computepay(hours,rate):
    print(" total work hours of employee = ",hours,"rate of pay = ",rate)
    if hours > 40:
        return rate * 40 + rate * 1.5 * (hours - 40)
    else:
        return hours * rate
try:
    hours = float(input("Enter hours: "))
    rate = float(input("Enter rate: "))
except ValueError:
#for text colouring we used ANSI escape code ;here the colour is red
    print("\033[1;32m Error, Please make sure to enter the value again......")
    quit()
p = computepay(hours, rate)
print('\033[0;31;47m Pay:', p)