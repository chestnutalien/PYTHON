#!/usr/bin/env python3

import sys
import re

if len(sys.argv) == 3:
    p1 = sys.argv[1]
    p2 = sys.argv[2]

    res = re.findall(p1, p2)
    print(len(res))
else:
    print("none")
