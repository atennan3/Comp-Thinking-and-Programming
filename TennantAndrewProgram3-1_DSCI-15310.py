# Andrew Tennant
# DSCI-15310-001 -- Computational Thinking and Programming
# Due Date -- 10/10/2017
# Program #1 -- Point of Pizza Sale: Taken or Picked Up?
# Determines the whether the customer received a deal or got ripped off

import math

print("Your local pizza shop ran out of large pizzas but have 2 mediums instead \nLet's see if they're giving you a deal or ripping you off.")

#Area of a large pizza
lRadius = float(input("What is the diameter of a large pizza in inches? "))/2
lArea = math.pi*(lRadius**2)

#Area of a medium pizza
mRadius = float(input("What is the diameter of a medium pizza in inches? "))/2
mArea = math.pi*(mRadius**2)

if lArea > (mArea * 2):
    print("You got ripped off!")
else:
    print("You got a deal!")
