# Andrew Tennant
# DSCI-15310-001 -- Computational Thinking and Programming
# Due Date -- 12/10/2017
# Program # 11 -- Prime Number Generator
# Determines whether a number, from a given range, is a prime number.


import random

def main () :
    quantity = int(input("How many random numbers would you like to generate? "))

    print('Getting ', quantity, "numbers between 1 and 1000.\n")

    for count in range (quantity):
        # Get a random number.
        number = random.randint(1, 1000)

        if number == 1:
            print(number, "is not a prime number.")
        elif number == 2 or number == 3 or number == 5 or number == 7:
            print(number, "is a prime number.")
        elif number % 2 != 0 and number %3 != 0 and number % 5 != 0 and number % 7 != 0:
            print(number, "is a prime number.")
        else:
            print(number, "is not a prime number.")

# Call the main function
main()
