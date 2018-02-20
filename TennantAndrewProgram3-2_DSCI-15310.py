# Andrew Tennant
# DSCI-15310-001 -- Computational Thinking and Programming
# Due Date -- 10/10/2017
# Program #2 -- 1089 and All That
# Produces the sum of two three-digit numbers, as 1089

import sys

num = int(input('Enter a 3-digit number: '))
print('Alright, assuming the first and third digits differ by 2 or more, check out this magic \n')

if (num >= 100 and num <= 999):
    numStr = str(num) # num converted to a string

    print('First, we are going to swap the first and second digits.')
    swapStr = numStr[2]+numStr[1]+numStr[0] # first and third digits are swapped
    print('That gives us', swapStr+'.')

    print('Then, we subtract that number from your original number.')
    swapNum = int(swapStr) # the swapped number is converted to an int for arithmetic
    subNum = num - swapNum # the swapped number is subtracted from the original

    if (subNum <= 99):
        print('Your first and third digits did not differ by more than two, so this will not work.')
        sys.exit()
    print('That results in', subNum, '.')

    subStr = str(subNum) # the result from subtraction is converted to a string for swapping
    subSwapStr = subStr[2]+subStr[1]+subStr[0] # swap is executed

    print('Swap the first and second digits of that number, too.')
    print('That makes', subSwapStr, '.')
    print('Then we add those two together.')

    subInt = int(subSwapStr)
    finalNum = subNum + subInt

    print('And we get', finalNum)
    if (finalNum != 1089):
        print('Wait a second, that isnt right, your first and third digits did not differ by two.')
else:
    print('Your number did not meet the criteria.')
