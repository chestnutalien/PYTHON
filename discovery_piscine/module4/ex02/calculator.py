#!/usr/bin/env python3
# ensure this program is executable 'chmod +x filename.py'

# prompt the user to enter two numbers
# store these numbers as numeric values in two variables
num1 = int(input("Give me the first number: "))
num2 = int(input("Give me the second number: "))
print("Thank you!")

# display the result of adding, subtrackting, dividing and multiplying these numbers
print(f"{num1} + {num2} = {num1+num2}")
print(f"{num1} - {num2} = {num1-num2}")
print(f"{num1} / {num2} = {num1/num2}")
print(f"{num1} * {num2} = {num1*num2}")
