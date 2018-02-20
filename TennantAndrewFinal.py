# Andrew Tennant
# DSCI-15310-001 -- Computational Thinking and Programming
# Due Date -- December 15, 2017
# Final Exam Program
# Trivia Test

# This program asks the user 10 questions, of which they must answer 6 correctly to pass.

def main():

    #introduce myself and get user name
    name = input("Hello, my name is Andrew. What it your name?\t")

    print("It's nice to meet you,", name,". \nLet's take a test.\nI'm going to ask you ten questions. Let\'s see how you do. \n\nOh, and please round all of your numerical answers to two places.\n")

    score = 0

    # Question 1
    one = float(input("What is the value of π?\t"))
    if one == 3.14:
        score = score + 1
        print("Nice,", name, "that's right!\n")
    else:
        print("Sorry,", name, ", the right answer is 3.14\n")

    # Question 2
    two = float(input("What is the value of φ?\t"))
    if two == 1.61:
        score = score + 1
        print("Nice,", name, "that's right!\n")
    else:
        print("Sorry,", name, ", the right answer is 1.61.\n")

    # Question 3
    three = float(input("What is the value of e, the Euler number?\t"))
    if three == 2.72:
        score = score + 1
        print("Nice,", name, "that's right!\n")
    else:
        print("Sorry,", name, ", the right answer is 2.72.\n")

    # Question 4
    four = float(input("What is the value of C, the Euler constant?\t"))
    if four == 0.58 or .58:
        score = score + 1
        print("Nice,", name, "that's right!\n")
    else:
        print("Sorry,", name, ", the right answer is 0.58.\n")

    # Question 5
    five = int(input("What is the largest digit in Base 2?\t"))
    if five == 1:
        score = score + 1
        print("Nice,", name, "that's right!\n")
    else:
        print("Sorry,", name, ", the right answer is 1.\n")
    # Question 6
    six = int(input("What is the largest digit in Base 8?\t"))
    if six == 7:
        score = score + 1
        print("Nice,", name, "that's right!\n")
    else:
        print("Sorry,", name, ", the right answer is 7.\n")

    # Question 7
    seven = str(input("What is the largest digit in base 16?\t"))
    if seven == "f" or "F":
        score = score + 1
        print("Nice,", name, "that's right!\n")
    elif seven != "f" or "F":
        print("Sorry,", name, ", the right answer is F.\n")

    # Question 8
    eight = float(input("What is the value of the multiplier effect in economics?\t"))
    if eight == 2.50:
        score = score + 1
        print("Nice,", name, "that's right!\n")
    else:
        print("Sorry,", name, ", the right answer is 2.50.\n")

    # Question 9
    nine = int(input("If 100 is reduced by 10%, what is the result?\t"))
    if nine == 90:
        score = score + 1
        print("Nice,", name, "that's right!\n")
    else:
        print("Sorry,", name, ", that's the wrong answer.\n")

    # Question 10
    ten = int(input("If the result of question 9 is increased by 10%, what is the new result?\t"))
    if ten == 99:
        score = score + 1
        print("Nice,", name, "that's right!\n")
    else:
        print("Sorry,", name, ", that's wrong. The result of question 9 is 90, and 90 increased by 10% is 99.\n")

    # Pass or Fail?
    if score >= 6:
        print("Congratulations, you passed with,", score, "questions right!")
    else:
        print("Sorry,", name, "you missed", 10-score, "questions. So you didn't pass.")
main()
