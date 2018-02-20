# Andrew Tennant
# DSCI-15310-001 -- Computational Thinking and Programming
# Due Date -- 10/31/2017
# Program #6 -- Odd Number Selector
# Displays the odd numbers in the range from 1 to 12

print("This program will display only the odd number in the range of 1 to 12.")

for number in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
    if (number % 2) == 1:
        print(number)
