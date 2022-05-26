# HackerRank 
# 1 Week Preparation Kit
# Created by: Ranit Pradhan
# Date: 25.05.2022

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
    # Write your code here
    count_plus=0
    count_minus=0
    count_zero=0
    for i in range(n):
        if(arr[i]<0):
            count_minus=count_minus+1
        elif(arr[i]==0):
            count_zero=count_zero+1
        else:
            count_plus=count_plus+1
    print(format(count_plus/n,".6f")) # taking upto 6 decimal points
    print(format(count_minus/n,".6f"))
    print(format(count_zero/n,".6f"))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))[:n]

    plusMinus(arr)
