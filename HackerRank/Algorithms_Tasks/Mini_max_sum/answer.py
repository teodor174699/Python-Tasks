#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    max,min=0,0
    
    arr.sort()
    for x in range(0,len(arr)):
        max = max + arr[x] 
    max = max - arr[0]
    
    arr.reverse()
    for x in range(0,len(arr)):
        min = min + arr[x]
    min = min - arr[0]
    
    
    
    print(min,max)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

