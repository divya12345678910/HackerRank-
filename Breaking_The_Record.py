#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    maxVal = 0
    minVal = 0
    maxbreak = 0
    minbreak = 0
  
    for score in scores:
        if maxVal < score:
            maxVal = score
            maxbreak += 1
        if minVal > score:
            minVal = score
            minbreak += 1
    return maxbreak, minbreak
      

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
