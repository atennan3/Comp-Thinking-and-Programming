# Andrew Tennant
# DSCI-15310-001 -- Computational Thinking and Programming
# Due Date -- November 9, 2017
# Program #8 -- Append File 1
# Appends mathematicians.txt


def main ():

    # Open mathematicians.txt

    outfile = open('mathematicians.txt', 'a')

    # Write the names of the mathematicians to the file

    outfile.write('John Venn\n')
    outfile.write('Pierre de Fermat\n')
    outfile.write('Maria Gaetana Agnesi\n')

    # Close the file

    outfile.close()

main()
