#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    
    for x in range(1,n+1):
        text="#" * x
        if n == x:
            print(text)
            continue
        space=" " * (n-x-1)
        print(space,text)
    

        
if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
