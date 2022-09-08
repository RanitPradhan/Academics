#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    new_str = ''
    temp = []
    for alpha in s:
        if ord(alpha)>=65 and ord(alpha)<=90:
            temp.append(chr(65+ (ord(alpha) -65 +k) %26))
        elif ord(alpha) >=97 and ord(alpha)<=122:
            temp.append(chr(97 + (ord(alpha) - 97 +k) %26))
        else:
            temp.append(alpha)
    new_str = new_str.join(temp)
    return(new_str)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
