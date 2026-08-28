#!/usr/bin/env python3
import sys

def shrink(txt):
    print(txt[0:8])

def enlarge(txt):
    print(txt, end="")
    length = 8 - len(txt)
    for x in range (length):
          print("Z", end="")
    print()

arg = sys.argv[1:]

if len(sys.argv) < 2:
    print("none")
else:
    # loops through each param 
    for arg in sys.argv[1:]:
        if len(arg) > 8:
            shrink(arg)
        elif len(arg) < 8:
            enlarge(arg)
        else:
            print(arg)