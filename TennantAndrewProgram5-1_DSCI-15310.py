# Andrew Tennant
# DSCI-15310-001 -- Computational Thinking and Programming
# Due Date -- 10/24/2017
# Program #5 -- Palindrome
# Determines how many numbers in a given range of 5-digit numbers are plaindromes

print('This program will list all five-digit palindromes are in a given range of numbers')

# Acquire range
first = int(input('Input the first five-digit number in the range. ' ))
last = int(input('Input the last five-digit number in the range. '))


count = 0

while first <= last:

    first = str(first)

    if first[0] == first[4] and first[1] == first[3]:
        count = count + 1
        print(first)

    first = int(first)
    first = first + 1

print(count, 'five-digit palindromes have been found.')

input('Press enter to exit.')
