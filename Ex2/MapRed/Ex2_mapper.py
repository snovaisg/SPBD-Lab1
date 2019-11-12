#!/usr/bin/env python3

# import sys
import sys
# import string library function  
import string 

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split(",")
    dis_type = words[3]
    region = words[6]
    print(f"({dis_type},{region})\t1")
