#!/usr/bin/env python3
# ensure this program is executable 'chmod +x filename.py'

# prompt the user to enter their age
age = input("Please tell me your age: ")
age = int(age)

# display the user's current age
print(f"You are currently {age} years old")

# display their age in 10, 20 and 30 yrs
mlist = [10, 20, 30]
for yrs in mlist:
    print(f"In {yrs} years, you'll be {yrs+age} years old")