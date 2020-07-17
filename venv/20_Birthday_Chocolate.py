'''
HackerRank: Easy
'''

def birthday(s, d, m):
    currentTotal = 0
    combinations = 0

    for i, num in enumerate(s):
        if sum(s[i:i+m]) == d:
            combinations += 1



    return combinations