#!/usr/bin/env python3

num = input("Enter a number less than 25\n")
num = int(num)

if num > 25:
    print("Error")
else:
    while num < 26:
        print(f"Inside the loop, my variable is {num}")
        num += 1