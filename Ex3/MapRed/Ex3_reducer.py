#!/usr/bin/env python3

# import sys
import sys
# import string library function  
import string 
from utils import Emit

is_first = True
curr_decade = ''
curr_continent = ''
curr_disaster = ''

curr_total_affected = 0
curr_total_deaths = 0
curr_injured = 0

def calculate_probas(injured, deaths, total_affected):
    """
    calculates probabilities of dying and being injured
    regarding total_affected.
    """
    
    # Sometimes there's no data and we 
    # don't want to divide by 0.
    if injured == deaths == total_affected == 0:
        death_proba = 0
        injured_proba = 0
    else:
        death_proba = deaths / total_affected
        injured_proba = injured / total_affected
    return injured_proba, death_proba

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into key,value
    keys,values = line.split('\t')
    # separate compositeKey
    continent, disaster, decade = eval(keys)
    injured, total_deaths, total_affected = eval(values)
    
    if is_first:
        is_first = False
        curr_decade = decade
        curr_continent = continent
        curr_disaster = disaster
        
        curr_total_affected += total_affected
        curr_total_deaths += total_deaths
        curr_injured += injured
        continue
    
    if decade != curr_decade or continent != curr_continent or disaster != curr_disaster:
        
        injured_proba, death_proba = \
            calculate_probas(curr_injured, curr_total_deaths, curr_total_affected)

        print(f"({disaster},{continent},{decade}),injured_proba: {injured_proba:.3f}")
        print(f"({disaster},{continent},{decade}),death_proba: {death_proba:.3f})")
        
        curr_decade = decade
        curr_continent = continent
        curr_disaster = disaster
        
        curr_total_affected = total_affected
        curr_total_deaths = total_deaths
        curr_injured = injured
        continue
# print the last one

injured_proba, death_proba = \
    calculate_probas(curr_injured, curr_total_deaths, curr_total_affected)
print(f"({disaster},{continent},{decade}),injure_proba: {injured_proba:.3f}")
print(f"({disaster},{continent},{decade}),death_proba: {death_proba:.3f})")
