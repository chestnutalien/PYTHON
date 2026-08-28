#! /usr/bin/env python3

import sys

# store the command-line arguments in a list
arg = sys.argv
# change the argument to string
txt = str(arg[1])
# count how many 'z' are in the string
amt = txt.count("z") 

if len(arg) != 2 and amt <1:
    print("none")
else:
   # for every z in the text print z
   for char in range(0,amt,1):
#    for char in txt:
#        if char == "z":
#             print("z", end="")
     print("z", end="")
   print()  

