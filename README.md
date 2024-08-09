# README

## First code

This is a repository where I am trying my first codes in Python

This is a calculator I have made in python as my first project

```python
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
```
Well this is one of my first projects and I am thinking I have actually made something big

This website is currently not that big as I dont know Python fully . This website will get edited and updated


all credits goes to Arnish and a mysterious man


