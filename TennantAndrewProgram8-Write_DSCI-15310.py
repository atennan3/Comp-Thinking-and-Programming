# Andrew Tennant
# DSCI-15310-001 -- Computational Thinking and Programming
# Due Date -- November 9, 2017
# Program #8 -- Write File
# Writes a file containing the names of three mathematicians

def main() :
    # Open file named mathematicians.txt

    outfile = open('mathematicians.txt', 'w')

    # Write to the file

    outfile.write('Benjamin Banneker\n')
    outfile.write('Stefan Banach\n')
    outfile.write('Omar Khayyam\n')

    # Close the file

    outfile.close()

main()
