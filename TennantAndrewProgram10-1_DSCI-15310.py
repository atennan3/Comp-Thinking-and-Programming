# Andrew Tennant
# DSCI-15310-001 -- Computational Thinking and Programming
# Due Date -- November 28, 2017
# Program #10 -- Append File for Program Number 9
# Appends Programmers.txt based on user input.

def main ():

    # Get the number of records you want to append
    num = int(input('How many records would you like to append to the file \'programmers.txt\'?'))

    # Open Programmers.txt
    programmers = open('programmers.txt', 'a')

    # Get data for each line and write it to the file
    for count in range (1, num + 1):
        print('Enter the name of programmer #' + str(count))

        name = input('Name: ')
        country = input('Nationality: ')
        cont = input('What was their contribution: ')

        #Write the data to the file
        programmers.write(name + '\n')
        programmers.write(country + '\n')
        programmers.write(cont + '\n\n')

        #Insert a blank line
        print()

    programmers.close()

    print ('Records appended to programmers.txt')

main()
