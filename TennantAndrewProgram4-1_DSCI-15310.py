# Andrew Tennant
# DSCI-15310-001 -- Computational Thinking and Programming
# Due Date -- 10/17/2017
# Program #4 -- Function Calculator
# Performs a series of calculations.

import math

def square(num):
    print (num, "squared is", (num*num))
    
def cube(num):
    print(num, "cubed is", (num*num*num))
    
def sqrRoot(num):
    print("The square root of", num, "is", (num**(.5)))
    
def cubeRoot(num):
    print("The cube root of", num, "is", (num**(1. / 3)))
    
def area(diam):
    print("The area is", (math.pi*((diam/2)**2)) )


num1 = float(input("What is the number you want squared? "))
square(num1)

num2 = float(input("What is the number you want cubed? "))
cube(num2)

num3 = float(input("Of which number do you want the square root? "))
sqrRoot(num3)

num4 = float(input("Of which number do you want the cube root? "))
cubeRoot(num4)

num5 = float(input("What is the diameter of the circle of which you want the area? "))
area(num5)
