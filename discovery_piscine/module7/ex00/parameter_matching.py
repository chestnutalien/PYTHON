#!/usr/bin/env python3
import sys

# store the command-line arguments in a list
arg = sys.argv
# if the number of params passed is different from 1 
# (excluding the script name itself)
if len(arg)!=2: 
    # if correct print none
    print("none")
else:
   # prompt the user to input the command-line argument 
   inpt = input("What was the parameter? ")   
   # change the target argument to string 
   arg = str(arg[1])
   # check if the user's input matches the argument    
   if inpt == arg: 
       # if correct print good job    
       print("Good job!") 
       # if incorrect print no, sorry    
   else:
       print("No, sorry...")