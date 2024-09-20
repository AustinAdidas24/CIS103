#CIS 103: Fundamentals of Programming
#Lab 2: Building a Simple Calculator
#Instructor: MD.Ali
#Student Name: Raul Violante
#Date: 09/11/2024
#Description:
#This script aims to create a calculator in which the four basic arithmetic operations can be performed like addition, subtraction, multiplication, and division
#
#Define the addition function
# -def add defines the function named add that takes two arguments, a and b. The def function keyword tells python we're defining a new function
# -return sends the result of the addition (a + b) back to the place where the function was called.
# defines the addition function for num1 and num2
#return function returns the sum of num1 and num2 to the calling code
def add(num1, num2):
    return num1 + num2
# Define the subtraction function
# returns the difference between num1 and num2
def subtract(num1, num2):
    return num1 - num2
# Define the multiplication function
# returns the product of num1 and num2
def multiply(num1, num2):
    return num1 * num2
# Define the division function
# Checks if num2 is zero to prevent division by zero, which would cause an error
# 1st return function returns an error message to notify the user that trying to divide by zero is invalid
# 2nd return function returns the division of num1 and num2
def divide(num1, num2):
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
# Provided user interface and use a loop
# def calculator defines the calculator function that will control the calculators operation and user interface
# while true creates a loop that will keep the program running until the user decides to end the script
def calculator():
    while True:
        print("Choose The Operation")
        print("+ ADD")
        print("- SUBTRACT")
        print("* MULTIPLY")
        print("/ DIVIDE")
        print("Type 'end' to Exit")
#print function here displays the function options for the user to select.
        function = input("Enter your your choice (+,-,*,/,end): ")
# function = input(input( prompts the user to select the operation.
        if function == 'end':
            print("Closing Out Calculator")
            break
# if function is if the user types 'end', the program will execute this block\
        # prints the message to indicating that the program is ending
        # (break)  breaks the loop
        if function in ['+','-','*','/']:
            num1 = float(input("First #: "))
            num2 = float(input("Second #: "))
# the if function here serves to check the user input
            #input function is asking the user to enter the first and second # and then the input is converted into a
            #float function handles both integers and decimals.
            if function == '+':
                print(num1, "+", num2, "=", add(num1, num2))
            elif function == '-':
                print(num1, "-", num2, "=", subtract(num1, num2))
            elif function == '*':
                print(num1, "*", num2, "=", multiply(num1, num2))
            elif function == '/':
                print(num1, "/", num2, "=", divide(num1, num2))
                # checks which operation the user selected
            #Check if user wants to continue
            #Break the while loop if no
            again = input("Do you want to perform another calculation? (yes/no): ")
            if again == "no":
                print("Exiting Calculator")
                break
        else:
            print("Invalid Input")
        # else is used if the user inputs something else other than the provided options
        # and prints Invalid Input
#Run the calculator by calling the calculator() function
calculator()

# operation = input( )
#
# if operation == "ADD":
#     num1 = input("Enter first number: ")
#     num2 = input("Enter second number: ")
#     print("The sum is " + str(int(num1) + int(num2)))
# elif operation == "SUBTRACT":
#     num1 = input("Enter first number: ")
#     num2 = input("Enter second number: ")
#     print("The difference is " + str(int(num1) - int(num2)))
# elif operation == "MULTIPLY":
#     num1 = input("Enter first number: ")
#     num2 = input("Enter second number: ")
#     print("The product is " + str(int(num1) * int(num2)))
# elif operation == "DIVIDE":
#     num1 = input("Enter first number: ")
#     num2 = input("Enter second number: ")
#     if num2 == 0:
#         print("Error Division By Zero")
#     else:
#         print("The result is " + str(int(num1) / int(num2)))