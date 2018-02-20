# Andrew Tennant
# DSCI-15310-001 -- Computational Thinking and Programming
# Due Date -- 11/2/2017
# Program # 7 -- Cube root, square root, cubae, and square calculator
# Displays the cube root, cube, square root, and square of numbers in a range
    #from 1 to 15, incremented by 2.

print("Number\t\t Cube-Root\t Cube\t\t Square-Root\tSquare")
print("-------------------------------------------------------------------------")

for number in range (1, 16, 2):
    cRoot = round(number ** (1.0/3.0), 2)
    cube = round(number ** 3, 2)
    sRoot = round(number ** (1.0/2.0), 2)
    square = round(number ** 2, 2)
    print(number, '\t\t', cRoot, '\t\t', cube, '\t\t', sRoot, '\t\t', square)

