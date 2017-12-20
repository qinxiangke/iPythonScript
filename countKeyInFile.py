#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

#calculate how many the key happens in the specific file
#Input:key is the object we want to calcualte
#******file is the scope we search
#Return:how many the key happens in the specific file
def countKeyInFile(key,file):
    with open(file, 'r') as f:
        lines = f.readlines()
        num=0
        for line in lines:
            length=len(line)
            num+=line.count(key,0,length)
    return num

count=countKeyInFile(sys.argv[1], sys.argv[2])
print(count)
