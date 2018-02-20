# Andrew Tennant
# DSCI-15310-001 -- Computational Thinking and Programming
# Due Date -- November 14, 2017
# Program #9 Write File
# Creates a database of famous programmers

def main():

    #Get the number of records for programmers you want to make
    numProg = int(input('How many records of programmers do you want to make? '))

    #Create the file for writing
    programmers = open('programmers.txt', 'w')

    #Get data for each line and write it to the file
    for count in range (1, numProg + 1):
        print('Enter the name of economist #' + str(count))

        name = input('Name: ')
        country = input('Nationality: ')
        cont = input('What was their contribution: ')

        #Write the data to the file
        programmers.write(name + '\n')
        programmers.write(country + '\n')
        programmers.write(cont + '\n')

        #Insert a blank line
        print()

    programmers.close()

    print ('Records written to programmers.txt')

main()
