#!/usr/bin/env python3

# method that takes a name as a parameter and displays a welcome message
# set default param in case there are none passed
def greetings(param="Stranger"):
    if not isinstance(param, str):
        print("Error! It was not a name")
    elif param == "Stranger":
        print("Hello, noble stranger")
    else:
        print(f"Hello, {param}")



greetings("Alexandra")
greetings("Wil")
greetings()
greetings(42)