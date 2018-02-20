# Andrew Tennant
# DSCI-15310-001 -- Computational Thinking and Programming
# Due Date -- November 9, 2017
# Program #8 -- Append File 2
# Appends mathematicians.txt


def main ():

    # Open mathematicians.txt

    outfile = open('mathematicians.txt', 'a')

    # Write the names of the mathematicians to the file

    outfile.write('David Hilbert\n')
    outfile.write('Henri Poincare\n')
    outfile.write('Bernhard Riemann\n')
    outfile.write('Niels Henrik Abel\n')

    # Close the file

    outfile.close()

main()
