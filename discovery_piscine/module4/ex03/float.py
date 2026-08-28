#!/usr/bin/env python3
# ensure this program is executable 'chmod +x filename.py'

# prompt the user to enter a number
num = float(input("Give me a number: "))

# determine if the entered number is a decimal or not and display the results
if num.is_integer():
    print("This number is an integer")
else:
    print("This number is a decimal") 