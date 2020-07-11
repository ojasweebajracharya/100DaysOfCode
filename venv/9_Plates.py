'''
Google Kickstart Round A 2020 Q2

N = numStacks
K = platesInStack
P = neededPlates

Note to self:
- Fix neededPlates and inc. into function

'''
import numpy as np

def maxSumBeauty(index, platesBeauty, plateCounter):
    organiseArr = []
    sortedArr = sorted(platesBeauty[i])
    highestNum = sortedArr[platesInStack - 1]
    currentRow = platesBeauty[index]
    print(f"currentRow {currentRow}")
    idxHighest = currentRow.index(highestNum)
    print(f"idxHighest {idxHighest}")
    sumToHighest = sum(currentRow[0:idxHighest + 1])

    print(f"sumOfi: {sumToHighest}")
    organiseArr.append([idxHighest, highestNum, sumToHighest, index])
    print(f"organiseArr {organiseArr}")


    # for i in range(numStacks):
    #     sortedArr = sorted(platesBeauty[i])
    #     highestNum = sortedArr[platesInStack - 1]
    #     platesBeautyArr = np.array(platesBeauty)
    #     # print(f"platesBeautyArr {platesBeautyArr}")
    #     # print(f"platesBeauty {platesBeauty}")
    #     currentRow = platesBeauty[i]
    #     print(f"currentRow {currentRow}")
    #     idxHighest = currentRow.index(highestNum)
    #     print(f"idxHighest {idxHighest}")
    #     sumToHighest = sum(currentRow[0:idxHighest + 1])
    #     # sumToHighest = currentRow[0:idxHighest].sum()
    #
    #     print(f"sumOfi: {sumToHighest}")
    #     organiseArr.append([idxHighest, highestNum, sumToHighest, i])
    #     print(f"organiseArr {organiseArr}")

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

    k = 0
    index = 0
    plateCounter = neededPlates
    while found != neededPlates and k <= numStacks:
        currentMatrix = maxSumBeauty(index, platesBeauty, plateCounter)

        current2D = np.array(currentMatrix)  # Gets rid of the commas, can use with numpy now
        sortedMat = current2D[current2D[::-1, 2].argsort()]

        print(f"SortedMat[k][2] {sortedMat[k][2]}")
        # total += sortedMat[k][2]
        #
        # found += sortedMat[k][0] + 1
        k += 1
        plateCounter -= currentMatrix[i[0]] + 1


    # while current[0] != neededPlates:
    #     new = maxSumBeauty(platesBeauty)
    #     current[0] += new[0]



    # print("Case #{}: {}".format(i, maxSumBeauty(platesBeauty)))





