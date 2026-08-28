#!/usr/bin/env python3
import sys

# store the command-line arguments in a list
arg = sys.argv

# if no parameters are provided, display "none
if len(arg)<2:
    print("none")
else:
   # print the total number of arguments passed (excluding the script name)
   print(f"parameters: {len(arg)-1}")
      # loop through the arguments starting from index 1 up to the last argument
   for a in range(1,len(arg),1):
       # print each argument along with its character length
       print(f"{arg[a]}: {len(arg[a])}")
       
