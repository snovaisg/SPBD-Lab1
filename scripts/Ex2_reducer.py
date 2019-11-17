#!/usr/bin/env python3

# import sys
import sys
# import string library function  
import string 


def Emit(key: str, value: str, sep='\t'):
    """
    Emmits a key-value pair.
    """
    message = f'{key}' + sep + f'{value}'
    print(message)

is_first_dis_type = True
curr_dis_type = ''
regions = []
# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # remove punctuation
    line = line.translate(str.maketrans('', '', string.punctuation))

    # separate compositeKey,value
    dis_type, region = line.split('\t')
    
    if is_first_dis_type:
        is_first_dis_type = False
        curr_dis_type = dis_type
        regions = [region]
        continue
        
    if dis_type != curr_dis_type:
        regions = list(set(regions))
        Emit(curr_dis_type, regions)
        regions = [region]
        curr_dis_type = dis_type
        continue
    regions.append(region)

regions = list(set(regions))
Emit(curr_dis_type, regions)
