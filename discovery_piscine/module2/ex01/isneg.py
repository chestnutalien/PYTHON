#!/usr/bin/env python3

number = input("Input number: ")

if int(number) == 0:
    print("This number is both positive and negative")
elif int(number) > 0:
    print("This number is positive")
else:
    print("This number is negative")