#!/usr/bin/env python3

import sys

if len(sys.argv) > 2:
    lst = sys.argv[1:]
    rev = lst[::-1]
    # print("\n".join(rev))

    for i in rev:
        print(i) 
else:
    print("none")