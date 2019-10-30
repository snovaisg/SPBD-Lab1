#!/usr/bin/env python3

# import sys
import sys
# import string library function  
import string 
from utils import Emit

is_first_continent = True
count = 0
curr_continent = ''

# input comes from STDIN (standard input)
for line in sys.stdin:
    # split the line into words
    continent,occurences = line.split("\t")
    
    if is_first_continent:
        curr_continent = continent
        count = int(occurences)
        is_first_continent = False
        
    elif curr_continent == continent:
        count += int(occurences)
    else:
        Emit(curr_continent,str(count))
        count = 0
        curr_continent = continent

Emit(curr_continent, str(count))
