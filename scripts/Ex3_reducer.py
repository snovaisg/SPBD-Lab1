#!/usr/bin/env python3

# import sys
import sys
# import string library function  
import string 

# Utility functions

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


is_first_key = True
curr_joint_keys = ''

curr_total_affected = 0
curr_total_deaths = 0
curr_injured = 0

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into key,value
    jointKeys,jointValues = line.split('\t')
    # separate values
    injured, total_deaths, total_affected = [int(e) for e in jointValues.split('_')]
    
    if is_first_key:
        is_first_key = False
        curr_joint_keys = jointKeys
        
        curr_total_affected += total_affected
        curr_total_deaths += total_deaths
        curr_injured += injured
        continue
    
    if curr_joint_keys != jointKeys:
        
        injured_proba, death_proba = \
            calculate_probas(curr_injured, curr_total_deaths, curr_total_affected)
    
        print(f"{jointKeys}, injured_proba: {injured_proba:.3f}")
        print(f"{jointKeys}, death_proba: {death_proba:.3f}")
        
        curr_joint_keys = jointKeys
        curr_total_affected = total_affected
        curr_total_deaths = total_deaths
        curr_injured = injured
        continue
        
    curr_total_affected += total_affected
    curr_total_deaths += total_deaths
    curr_injured += injured
        
# print the last one
injured_proba, death_proba = \
    calculate_probas(curr_injured, curr_total_deaths, curr_total_affected)
print(f"{jointKeys}, injured_proba: {injured_proba:.3f}")
print(f"{jointKeys}, death_proba: {death_proba:.3f}")
