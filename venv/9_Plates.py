'''
Google Kickstart Round A 2020

N = numStacks
K = platesInStack
P = neededPlates
'''

def maxSumBeauty(platesBeauty, stackCounter):
    for i in range(n)
    #format into {setnum}, {idx}, {sumbeforeit}]
    #return [found,sumsofar]


testCases = int(input())
platesBeauty = []
for i in range(testCases):
    numStacks, platesInStack, neededPlates = list(map(int, input().split(" ")))
    for j in range(numStacks):
        platesBeauty.append(list(map(int, input().split())))

    current = maxSumBeauty(platesBeauty, stackCounter)
    while current[0] != neededPlates:
        new = maxSumBeauty(platesBeauty, stackCounter)
        current[0] += new[0]

    print(current)
    # print("Case #{}: {}".format(i, maxSumBeauty(platesBeauty)))





