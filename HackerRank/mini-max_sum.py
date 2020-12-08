
import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr.sort()
    minsum = 0
    maxsum = 0
    
    for i in range(4):
        minsum += arr[i]
        maxsum += arr[i+1]
    
    print(minsum, maxsum)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
