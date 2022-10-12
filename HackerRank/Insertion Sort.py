# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 11:37:04 2022

@author: carme
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    output = [0] * (max(arr) + 1)
    
    for el in arr:
        output[el] += 1
        
    return output

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
