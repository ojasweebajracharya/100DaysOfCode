'''
HackerRank Question
'''

n = int(input())
counterSpace = n - 1
counterHash = 1

for i in range(n):
    print(" "*counterSpace + "#"*counterHash)
    counterHash += 1
    counterSpace -= 1