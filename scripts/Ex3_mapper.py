#!/usr/bin/env python3

# import sys
import sys
# import string library function  
import string 

# Utility functions
def Emit(key: str, value: str, sep='\t'):
    """
    Emmits a key-value pair.
    """
    message = f'{key}' + sep + f'{value}'
    print(message)

def nan_to_zero(a: str)->int:
    """
    Puts a zero string whenever the value is missing
    """
    if not a:
        return "0"
    return a

# input comes from STDIN (standard input)s

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
    
    joint_key = "_".join([disaster,continent,decade])
    joint_values = "_".join([str(injured), str(total_deaths), str(total_affected)])
    
    Emit(joint_key, joint_values)
