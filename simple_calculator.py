#Addition

import sys
try:
    num1 = int(input("Enter the first number"))
    num2 = int(input("Enter the second number"))
except: 
    print("Stupid human give me a proper number not a bullshit")
    sys.exit()
Addition = num1 + num2
print("The addition of the two numbers are " + str(Addition))

#Subtraction
Subtraction = num1 - num2
if num2 > num1:
    Subtraction = num2 - num1   
else:
    Subtraction = num1 - num2
print("The subtraction of the two numbers are " + str(Subtraction))

#Multiplication
Multiplication = num1 * num2
print("The multiplication of the two numbers are " + str(Multiplication))

#Division
try:
    Division = num1 / num2
    print("The division of the two numbers are " + str(Division))
except ZeroDivisionError:
    print("I cannot be divided by zero")
