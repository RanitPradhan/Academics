#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'powerSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER X
#  2. INTEGER N
#

def powerSum(X, N, num):
    # Write your code here
    value = X - num**N
    if value<0:
        return(0)
    elif value==0:
        return(1)
    else:
        return powerSum(value, N, num+1)+powerSum(X, N, num+1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    X = int(input().strip())

    N = int(input().strip())

    result = powerSum(X, N, 1)

    fptr.write(str(result) + '\n')

    fptr.close()
