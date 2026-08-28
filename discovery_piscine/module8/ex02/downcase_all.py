#!/usr/bin/env python3
import sys

# define a method called downcase_it
def downcase_it(txt):
    # # takes string and returns the string in lowercase
    return txt.lower()

# check if there are 2 params or more params (with file name)
if len(sys.argv) > 1:
    # loops through each param and makes it lowercase
    for x in sys.argv[1:]:
        print(downcase_it(str(x)))
# if there are no params additional params returns 'none'
else:
    print("none")
