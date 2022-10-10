#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    
    for n in range(0,len(grades)):
        
        if grades[n] < 38:
            continue
        else:
            oldG = grades[n]
            testG = oldG % 5
            if testG == 3:
                oldG += 2
                grades[n] = oldG
            elif testG == 4:
                oldG += 1
                grades[n] = oldG
            else:
                continue
    return grades

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
