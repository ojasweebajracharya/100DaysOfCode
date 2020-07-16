'''
HackerRank Question: Easy

- Need to revisit, got this from a tutorial.
'''
#!/bin/python3

import math
import os
import random
import re
import sys
from math import gcd
#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def gcd_list(nums):
    gcd_nums = None
    for i in range(len(nums)):
        if i == 0:
            gcd_nums = nums[i]
        else:
            gcd_nums = gcd(gcd_nums, nums[i])
    return gcd_nums


def lcm(a,b):
    return int(a * b / gcd(a,b))

def lcm_list(nums):
    lcm_nums = None
    for i in range(len(nums)):
        if i == 0:
            lcm_nums = nums[i]
        else:
            lcm_nums = lcm(lcm_nums, nums[i])
    return lcm_nums

def getTotalX(a, b):
    # Write your code here
    lcm_a = lcm_list(a)
    gcd_b = gcd_list(b)

    a_cms = []
    i = 1
    while True:
        temp = lcm_a * i
        if temp > gcd_b:
            break

        a_cms.append(temp)
        i += 1

    answer = 0
    for temp in a_cms:
        is_factor = True
        for bb in b:
            if bb % temp != 0:
                is_factor = False
        if is_factor:
            answer += 1

    return answer


print(getTotalX([2,4],[16,32,96]))