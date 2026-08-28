#!/usr/bin/env python3

import sys

# check if there are 3 params (with file name)
if len(sys.argv) != 3:
    print("none")
# # check if params (other than file name) are not ints
# elif sys.argv[1:] != int:
#     print("not int")
# check if the 2nd number is bigger than the 1st
elif int(sys.argv[1]) > int(sys.argv[2]):
    print("a > b")
else:
    # construct an array containing all the vaules between these two numbers
    arr = list(range(int(sys.argv[1]), int(sys.argv[2])+1))
    print(arr)