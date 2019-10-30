#!/usr/bin/env python
# import sys
import sys
# import string library function  
import string 
from utils import Emit

prev_dist=''
dic={}
regions=[]
for line in sys.stdin:
    # split the line into words
    line = line.translate(str.maketrans('', '', '\n'))
    dist_type,region = line.split("\t")
    
    c = dist_type + region
    
    if prev_dist!=dist_type:    
        Emit(prev_dist,regions)
        regions=[region]
        prev_dist=dist_type
        dic={c:True}

    elif c in dic:
        continue
    else:
        dic[c]=True
        regions.append(region)
        
