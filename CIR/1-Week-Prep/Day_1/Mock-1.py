# HackerRank 
# 1 Week Preparation Kit
# Created by: Ranit Pradhan
# Date: 26.05.2022

#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findMedian' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def findMedian(arr,n):
    # Write your code here
    arr=sorted(arr)
    r=n//2
    print(arr[r])
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = findMedian(arr,n)

    fptr.write(str(result) + '\n')

    fptr.close()
