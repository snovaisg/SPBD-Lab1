#!/usr/bin/env python3

# import sys
import sys
# import string library function  
import string 


curr_region = ''
is_first_dist_type = True
curr_dist_type = ''
regions = []
# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # separate compositeKey,value
    key,_ = line.split('\t')
    # remove  leading '(' and trailing ')'
    key = key[1:-1]
    # separate compositeKey
    dis_type,region = key.split(',')
    
    if is_first_dist_type:
        is_first_dist_type = False
        curr_dist_type = dis_type
        regions = [region]
        curr_region = region
        continue
        
    if dis_type != curr_dist_type:
        print(curr_dist_type+"\t"+str(regions))
        regions = [region]
        curr_region = region
        curr_dist_type = dis_type
        continue
        
    if region != curr_region:
        regions.append(region)
        curr_region = region

print(curr_dist_type+"\t"+str(regions))
