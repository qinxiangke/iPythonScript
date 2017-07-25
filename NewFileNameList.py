#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

#FunName:NewFileNameList()
#Description: create a file name list from the format of a file name per line to the format of a line containning all the files.
#Input:  infile  is represent for a file containning a file name list, a file name per line.
#Output:  outfile  is represent for a file containning a file name list, only occupying a line.
#Return:  FileNameList  is represent for a list containning all the file name.
def defFileNameList(infile, outfile):
    with open(infile, 'r') as f:
        lines = f.readlines()
        FileNameList='['
        for line in lines:
            line=line.strip('\n')
            FileNameList=FileNameList+'"'+line+'"'+','
        with open(outfile, 'w') as f:
                f.write(FileNameList)
        return FileNameList

defFileNameList(sys.argv[1], sys.argv[2])
#print(FileNameList)
