#!/usr/bin/env python3

# import sys
import sys
# import string library function  
import string 

# Utility function
def Emit(key: str, value: str, sep='\t'):
    """
    Emmits a key-value pair.
    """
    message = f'{key}' + sep + f'{value}'
    print(message)

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split(",")
    continent = words[5]
    occurrences = words[9]
    Emit(str(continent),str(occurrences))
