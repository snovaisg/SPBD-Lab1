#!/usr/bin/env python3

# import sys
import sys
# import string library function  
import string 
from utils import Emit

def nan_to_zero(a: str)->int:
    """
    Puts a zero string whenever the value is missing
    """
    if not a:
        return "0"
    return a

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split(",")
    
    continent = words[5]
    disaster = words[3]
    decade = words[0][:3] + '0'
    
    casualties = [int(nan_to_zero(a)) for a in words[10:15]]
    total_deaths, injured, affected, homeless, total_affected = casualties
    
    if total_affected < sum(casualties[:-1]):
        total_affected = sum(casualties[:-1])
    
    print(f"('{disaster}','{continent}','{decade}')\t{[injured, total_deaths, total_affected]}")
