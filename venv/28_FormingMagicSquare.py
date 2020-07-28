'''
HackerRank: Medium

Got help from YT
'''
import sys

def formingMagicSquare(s):
    # Convert 2D Matrix into 1D:
    s = sum(s, [])

    magic = [
            [8, 1, 6, 3, 5, 7, 4, 9, 2],
            [6, 1, 8, 7, 5, 3, 2, 9, 4],
            [4, 9, 2, 3, 5, 7, 8, 1, 6],
            [2, 9, 4, 7, 5, 3, 6, 1, 8],
            [8, 3, 4, 1, 5, 9, 6, 7, 2],
            [4, 3, 8, 9, 5, 1, 2, 7, 6],
            [6, 7, 2, 1, 5, 9, 8, 3, 4],
            [2, 7, 6, 9, 5, 1, 4, 3, 8],
            ]

    mincost = sys.maxsize

    for mag in magic:
        diff = 0
        for i,j in zip(s, mag):
            diff += abs(i-j)
        mincost = min(mincost, diff)
    return mincost