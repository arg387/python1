if __name__ == '__main__':
    n = int(input())
    i = 0
    
    while i < n:
        print(i*i)
        i += 1
        #i += 1 is under printing statement so print will start from 0 since i = 0 given before
def is_leap(year):
    if year % 4 == 0:
        leap =True
        if year % 100 == 0:
            leap= False
            if year % 400 == 0:leap = True
            else:leap = False
        else:leap = True
    else:leap = False
    return leap
year = int(input("Enter a year: "))
print(is_leap(year))

if __name__ == '__main__':
    n = int(input()) 
    for n in range(1,n+1):
        print(n,end="")


import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if 1<=n and n%2 != 0:
        print("Weird")
    if n%2 ==0 and 1<n<6:
        print("Not Weird")
    if n%2 ==0 and 5<n<21:
        print("Weird")
    if n%2 ==0 and 20<n<=100:
        print("Not Weird")