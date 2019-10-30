#!/usr/bin/env python3

# import sys
import sys
# import string library function  
import string 
from utils import Emit

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split(",")
    continent = words[5]
    occurrences = words[9]
    Emit(str(continent),str(occurrences))
