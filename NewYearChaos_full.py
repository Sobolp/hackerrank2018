#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    result = 0
    for i in range(len(q)):
        c = q[i] - (i + 1)
        if (c > 0) :
            if (c > 2):
                return 'Too chaotic'
            result = result + c
    return result

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)