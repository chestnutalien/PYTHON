#!/usr/bin/env python3

import sys

# loops through each param 
for arg in sys.argv[1:]:
    # checks the starting index of the string 
    ism = arg.find("ism")
    # check if ism was found AND it's at the end
    if ism != -1 and ism == len(arg) - len("ism"):
        continue    # skips if word ends with "ism" skip
    # print the argument and add ism at the end
    print(arg + "ism")