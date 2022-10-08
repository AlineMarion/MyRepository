#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lilysHomework' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#
def swapElements(arr, i, j):
    aux = arr[i]
    arr[i] = arr[j]
    arr[j] = aux
    
def getPairs(array, ordered):  
    pairs = []
    arr = array.copy()
    for i in  range(len(arr)):
        if(ordered[i] == arr[i]):
            continue
        else:
            for j in range(i, len(arr)):
                if(ordered[i] == arr[j]):
                    pairs.append([i, j])
                    swapElements(arr, i, j)
                    break
    return pairs
                    
def lilysHomework(arr):
    # Write your code here
    ordered = sorted(arr)
    reverse = ordered[::-1]
    ordered = len(getPairs(arr, ordered))
    reverse = len(getPairs(arr, reverse))
    if(reverse < ordered):
        return reverse
    else:
        return ordered               

if __name__ == '__main__':

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = lilysHomework(arr)

    print(result)

# 2 5 4 3 1
# 1 5 4 3 2
# 1 2 4 3 5
# 1 2 3 4 5
#
#
#
# 2 3 4 5 1
# 1 3 4 5 2
# 1 2 4 5 3
# 1 2 3 5 4
# 1 2 3 4 5
#
#