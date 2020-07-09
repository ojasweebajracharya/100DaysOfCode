'''
Google Kickstart Round A 2020

N = numStacks
K = platesInStack
P = neededPlates
'''
import numpy as np

def maxSumBeauty(platesBeauty):
    organiseArr = []
    for i in range(numStacks):
        sortedArr = sorted(platesBeauty[i])
        highestNum = sortedArr[platesInStack - 1]
        # sumOfi = sum(platesBeauty[i[:platesBeauty[i].index(highestNum)]])
        platesBeautyArr = np.array(platesBeauty)
        sumOfi = platesBeautyArr[:,platesBeautyArr[i].index(highestNum)]

        print(f"sumOfi: {sumOfi}")
        organiseArr.append([platesBeauty[i].index(highestNum), highestNum, sumOfi, i])

    return organiseArr
    # format returned : {idx of highest num}, highestnum, {sumbeforeit}, idxInOriginal]



# Main starts here:
    #return [found,sumsofar]
testCases = int(input())

for i in range(testCases):
    total  = 0
    found = 0

    platesBeauty = []
    numStacks, platesInStack, neededPlates = list(map(int, input().split(" ")))
    for j in range(numStacks):
        platesBeauty.append(list(map(int, input().split())))

    currentMatrix = maxSumBeauty(platesBeauty)

    current2D = np.array(currentMatrix) # Gets rid of the commas, can use with numpy now
    print(f"currentMatrix: {currentMatrix}")

    # Sorts in order of highest sum value:
    sortedMat = current2D[current2D[::-1,2].argsort()]
    print(f"sortedMat: {sortedMat}")

    k = 0
    while found != neededPlates and k <= numStacks:
        print(sortedMat[k][2])
        # total += sortedMat[k][2]
        #
        # found += sortedMat[k][0] + 1
        k += 1


    # while current[0] != neededPlates:
    #     new = maxSumBeauty(platesBeauty)
    #     current[0] += new[0]



    # print("Case #{}: {}".format(i, maxSumBeauty(platesBeauty)))





