# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 13:26:25 2022

@author: carme
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    
    noInput = int(input())
    theArray = list(map(int, input().split()))
    
    totalValue = [0]*100
    
    for i in range (0,noInput):
        n = ar[i]
        totalValue[n] += 1
    print(*tot, sep' ')

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
    