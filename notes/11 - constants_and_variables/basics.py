#-----------------------------------------------------------------------------
# Name:        Some Basics (basics.py)
# Purpose:     To provide a sample program about the basics of Python
#
# Author:      Mr. Seidel
# Created:     14-Aug-2018
# Updated:     28-Sep-2018
#-----------------------------------------------------------------------------

# Printing the addition of two integers
print(f'{1 + 2}')

# Printing of the subtraction of two floats
print(f'{4.3 - 2.1}')

# Boolean values
right = True
wrong = False
print(f'{right}')
print(f'{wrong}')

# Two integers to be used for the rest of the program.
integerOne = 1
integerTwo = 2

# Two float values to be used for the rest of the program.
floatOne = 3.14
floatTwo = 5.3

# Multiplying two float values.
productOfFloats = floatOne * floatTwo
print(f'{productOfFloats}')

# Division of two float values.
quotientOfFloats = floatTwo / floatOne
print(f'{quotientOfFloats}')

# Using integer division on two floats
integerDivisionOfFloats = floatTwo // floatOne
print(f'{integerDivisionOfFloats}')

# Using the modulo operator
moduloOfIntegers = 5 % 2
print(f'{moduloOfIntegers}')

# Converting between floats and integers
print(f'{int(floatOne)}')
print(f'{float(integerOne)}')

# Equation
print(f'{(4 * 2) / 8}')

# Getting input from the user using input('Question goes here')
# Then formatting and printing back out the user input.
name = input('Enter your name: ')  # Note: This asks the user to 'Enter your name: '.  Do NOT change this to your name directly
age = input('Enter your age: ')
print(f'Hello {name} you are {age} years old.')

