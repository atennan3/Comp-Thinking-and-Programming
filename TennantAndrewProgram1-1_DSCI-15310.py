# Andrew Tennant
# DSCI-15310-001 -- Computational Thinking and Programming
# 09/26/2017
# Program #2 -- Mortgage Calculator
# Calculates annual salary after a raise

# Get the current salary and raise percentage
originalSalary = float(input("What is your current salary?)\t$"))
raisePercentage = float(input("What is the percentage the wage will be raised? Express as a decimal.\t"))

# Calculate the new salary
newSalary = ((raisePercentage * originalSalary) / 100) + originalSalary
print("Your new salary is ", newSalary)
