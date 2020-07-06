'''
Google Kickstart Round A 2020

N = numStacks
K = platesInStack
P = neededPlates
'''

class Stack:
    def __init__(self):
        self.stack = list()

    def pushChar(self, ch):
        self.stack.append(ch)

    def popChar(self):
        return self.stack.pop()


def maxSumBeauty():
    pass


testCases = int(input())
for i in range(testCases):
    numStacks, platesInStack, neededPlates = list(map(int, input().split(" ")))
    for j in range(numStacks):
        platesBeauty = list(int, map(input().split()))
        print("Case #{}: {}".format(i, maxSumBeauty(platesBeauty)))



