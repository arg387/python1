def computepay(h, r):
    if h <= 40:
        pay = h * r 
    else:    
        pay = 40 * r + (h - 40) * 1.5 * r
    return pay

h = float(input("Enter Hours:"))

r = float(input("Enter Rate:"))


pay = computepay(h, r)
print("Pay", pay)

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
    except (ValueError, TypeError):
        print ("Error, please enter a numeric input")
        quit()

print(main(computepay(h, r)))