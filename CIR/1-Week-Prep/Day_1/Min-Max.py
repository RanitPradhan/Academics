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
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    arr=sorted(arr)
    i=0
    sum=0
    for i in range (len(arr)-1):
        sum=sum+arr[i]
    print(sum,end=' ')
    arr=arr[1:]
    sum=0
    for i in range(len(arr)):
        sum=sum+arr[i]    
    print(sum)
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
