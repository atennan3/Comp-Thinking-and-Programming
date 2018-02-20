# Andrew Tennant
# DSCI-15310-001 -- Computational Thinking and Programming
# Due Date -- 10/3/2017
# Program # Grade Calculator
# Determines a student's grade


# Get the original, lowest, and highest grades
orgGrade = int(input("What is the current numbered grade? "))
highGrade = int(input("What is the highest grade in the class? "))
lowGrade = int(input("What is the lowest grade in the class? "))

# Calculate the curve
curve = ((highGrade - lowGrade)/4) + orgGrade

finalGrade = chr

if (curve >= 90):
    finalGrade = 'A'
    print("The final grade is an", finalGrade, ".")
elif (curve >= 80) & (curve <= 89):
    finalGrade = 'B'
    print("The final grade is a", finalGrade)
elif (curve >=70) & (curve <= 79):
    finalGRade = 'C'
    print("The final grade is a", finalGrade)
elif (curve >= 60) & (curve<= 69):
    finalGrade = 'D'
    print("The final grade is a", finalGrade)
elif (curve < 60):
    finalGrade = 'F'
    print("The final grade is an", finalGrade)
