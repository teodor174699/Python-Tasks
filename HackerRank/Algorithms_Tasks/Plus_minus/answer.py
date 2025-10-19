#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    positive,negative,zero = 0,0,0
    for x in range(len(arr)):
        if arr[x] > 0:
            positive = positive + 1
            continue
        elif arr[x] < 0:
            negative = negative + 1
            continue
        elif arr[x] == 0:
            zero = zero + 1
            continue
        
    pr = float(positive/len(arr))
    nr = float(negative/len(arr))
    zr = float(zero/len(arr))
    
    print(f"{pr:.6f}")
    print(f"{nr:.6f}")
    print(f"{zr:.6f}")

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

