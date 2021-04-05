# Name: Your  First & Last  Name
# SSID: Student  ID  Number
# Assignment  #: 2
# Submission  Date: 3/16/2021
#
# Description  of  program:
# This is a trivia  quiz  about  computer  science
print("**************************************************")
print("Welcome  to the  Computer  Science  Trivia  Quiz..")
print("Win by  answering  all  three  questions  correctly")
print("**************************************************")

# variables to store the results of the answers
answer1 = False
answer2 = False
answer3 = False
# counter of the correct answers
counter = 0

# while loop keeps the app running while at least one of the answers is wrong
while (answer1 == False) or (answer2 == False) or (answer3 == False):
    # if the question 1 wasn't answered or was answered wrong this block is executed
    if not answer1:
        input1 = input("Q1: A variable in Python can store data of __________? \n1. only the same type \n2. only str type  \n3. different types \n4. only int type \nEnter your answer (1,2,3, or 4): \n")
        if int(input1) == 3:
            print("You’ve done your homework! That is correct.")
            counter += 1
            answer1 = True
        else:
            print("That is incorrect, let’s try another question")
    # if the question 2 wasn't answered or was answered wrong this block is executed
    if not answer2:
        input2 = input(
            "Q2: In Python what data type is the number 1.08 ? \n1. float \n2. int \n3. list \n4. str \nEnter your answer (1,2,3, or 4): \n")
        if int(input2) == 1:
            print("Terrific! You’ve been studying your algorithms!")
            counter += 1
            answer2 = True
        else:
            print("That is incorrect, let’s try another question")
    # if the question 3 wasn't answered or was answered wrong this block is executed
    if not answer3:
        input3 = input(
            "Q3: What is the output of the following code: print(type(\"5\"))? \n1. <class 'int'> \n2. <class 'list'> \n3. <class 'float'> \n4. <class 'str'> \nEnter your answer (1,2,3, or 4): \n")
        if int(input3) == 4:
            print("You are right!")
            counter += 1
            answer3 = True
        else:
            print("That is incorrect.")
    # checking if the counter of the correct answers reached 3
    # and breaking out of the loop if all the questions were answered correctly
    if (counter == 3):
        print("Great! You answered all the ", counter, " questions correctly")
        print("Thank you for playing. Goodbye")
        break
    # if some of the answeres were wrong the user is asked to try again or exit
    else:
        print("You answered ", counter, " out of 3 questions incorrectly")
        input4 = input("Do you want to try your incorrect answers again? (y)es or (n)no?:\n")
        if (input4 == 'n'):
            print("Thank you for playing. Goodbye")
            break
