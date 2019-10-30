#!/usr/bin/env python
# import sys
import sys
# import string library function  
import string 
from utils import Emit

dic={}
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    line = line.translate(str.maketrans('', '', '\n'))
    words = line.split(",")
    
    region = words[6]
    dist_type = words[3]
    c=dist_type+region
    if c in dic:
        continue
    else:
        dic[c]=True
        Emit(dist_type,region)
    
