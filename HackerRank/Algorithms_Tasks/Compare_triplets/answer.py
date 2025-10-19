#!/bin/python3

import math
import os
import random
import re
import sys
#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    arr1 = a
    arr2 = b
    score = [0,0]
    
    
    for x in range(len(arr1)):
        if arr1[x] > arr2[x]:
            score[0] = score[0] + 1 
            continue
        if arr1[x] < arr2[x]:
            score[1] = score[1] + 1
            continue
    return score
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

