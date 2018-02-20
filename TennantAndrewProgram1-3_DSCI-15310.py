# Andrew Tennant
# DSCI-15310-001 -- Computational Thinking and Programming
# 09/26/2017
# Program #3 -- Paint Usage Calculator
# This program calculates how much paint will be needed to paint a number of rooms


# Get the dimensions of all of the rooms
livingLength = int(input("Enter the length of the lving room: "))
livingWidth = int(input("Enter the width of thelLiving room: "))
kitchenLength = int(input("Enter the length of the kitchen: "))
kitchenWidth = int(input("Enter the width of the kitchen "))
diningLength = int(input("Enter the length of the dining room: "))
diningWidth = int(input("Enter the width of the dining room "))
masterLength = int(input("Enter the length of the master bed room: "))
masterWidth = int(input("Enter the width of the master bed room: "))
bed1Length = int(input("Enter the length of the first bed room: "))
bed1Width = int(input("Enter the width of the first bed room: "))
bed2Length = int(input("Enter the length of the second bed room: "))
bed2Width = int(input("Enter the width of the second bed room: "))

# Calculate amout of buckets needed for each room
living = ((livingLength*livingWidth)+(livingLength*12*2)+(livingWidth*12*2))/350
kitchen = ((kitchenLength*kitchenWidth)+(kitchenLength*12*2)+(kitchenWidth*12*2))/350
dining = ((diningLength*diningWidth)+(diningLength*12*2)+(diningWidth*12*2))/350
master = ((masterLength*masterWidth)+(masterLength*12*2)+(masterWidth*12*2))/350
bed1 = ((bed1Length*bed1Width)+(bed1Length*12*2)+(bed1Width*12*2))/350
bed2 = ((bed2Length*bed2Width)+(bed2Length*12*2)+(bed2Width*12*2))/350

total = living + kitchen + dining + master + bed1 + bed2

# Round the calculations
l = round(living,0)
k = round(kitchen,0)
d = round(dining,0)
m = round(master,0)
b1 = round(bed1,0)
b2 = round(bed2,0)
t = round(total,0)

print("You will need ", l, "gallons of paint for the living room.")
print("You will need ", k, "gallons of paint for the kitchen.")
print("You will need ", d, "gallons of paint for the dining room.")
print("You will need ", m, "gallons of paint for the master bedroom.")
print("You will need ", b1, "gallons of paint for the first other bedroom.")
print("You will need ", b2, "gallons of paint for the second other bedroom.")
print("You will need ", t, "gallons of paint in total.")



