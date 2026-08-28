#!/usr/bin/env python3

num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
res = int(num1) * int(num2)

print(f"{num1} x {num2} = {res}")

if res == 0:
    print("The result is positive and negative")
elif res > 0:
    print("The result is positive")
else:
    print("The result is negative")