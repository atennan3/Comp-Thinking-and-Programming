# Andrew Tennant
# DSCI-15310-001 -- Computational Thinking and Programming
# Due Date -- November 9, 2017
# Program #8 -- Read File
# Reads mathematicians.txt


def main() :

    # Open mathematicians.txt

    infile = open('mathematicians.txt', 'r')

    # Read the file contents

    contents = infile.read()

    # Close the file

    infile.close()

    # Print the file

    print(contents)

main()
