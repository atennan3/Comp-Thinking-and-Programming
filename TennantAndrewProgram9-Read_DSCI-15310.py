# Andrew Tennant
# DSCI-15310-001 -- Computational Thinking and Programming
# Due Date -- November 14, 2017
# Program #9 Read File
# Reads the programmer database

def main():
    programmers = open('programmers.txt','r')

    name = programmers.readline()

    while name !='':

        nation = programmers.readline()

        cont = programmers.readline()

        #Strip the new lines from the fields

        name = name.rstrip('\n')
        nation = nation.rstrip('\n')
        cont = cont.rstrip('\n')

        #Display record

        print('Name:', name)
        print('Nationality: ', nation)
        print('Contribution: ', cont)
        print()

        #Read the name field of the next record
        name = programmers.readline()

    programmers.close()

main()
