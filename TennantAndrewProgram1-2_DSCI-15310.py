# Andrew Tennant
# DSCI-15310-001 -- Computational Thinking and Programming
# 09/26/2017
# Program #2 -- Mortgage Calculator
# Calculates mortgage using the formaula: principal × rate / (1 – (rate + 1)-term)


# Gather variables
p = float(input("What is the principle?\t$"))
interest = float(input("What is your interest rate? Express as a decimal.\t"))
r = interest/100
t = float(input("How long is the term in years?"))

# Calculate yearly and monthly payment
payment = p*r/(1-(r+1)**(-t))
print("Your mortgage payment will be ", payment)

monthlyPayment = (p*(r/12))/(1-((r/12)+1)**(-1*(t*12)))
print("Your monthly payment will be ", monthlyPayment)
