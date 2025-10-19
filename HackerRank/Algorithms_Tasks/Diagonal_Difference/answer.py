#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    ld = 0
    rd = 0
    for x in range(len(arr)):
        ld = ld + arr[x][x]
        x + 1
    arr.reverse()
    for y in range(len(arr)):
        rd = rd + arr[y][y]
        y + 1

    
    # Write your code here
    
  
    
    if ld > rd:
        sum = ld - rd
    if ld <= rd:
        sum = rd - ld
    return sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

