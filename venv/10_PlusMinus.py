'''
HackerRank Question: Easy
'''

import math
import os
import random
import re
import sys
from decimal import Decimal


def plusMinus(arr):
    plusCount = 0
    minusCount = 0
    zeroCount = 0

    for i in arr:
        if i > 0:
            plusCount += 1
        elif i < 0:
            minusCount += 1
        elif i == 0:
            zeroCount += 1
        else:
            print("Error")

    print(round((Decimal(plusCount/n)),6))
    print(round((Decimal(minusCount/n)),6))
    print(round((Decimal(zeroCount / n)), 6))


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
