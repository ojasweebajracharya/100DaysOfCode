'''
Google Kickstart Round A 2020 Q2

N = numStacks
K = platesInStack
P = neededPlates

Note to self:
Test 1 Works !!!! Yaaayy
For test two, need to enumerate to get indexes and values and use a dict to retain last index.
Last repeated high number index is then stored.

(and this: )
To simplify:
max() exists -_-

'''
import numpy as np

def rowChecker(currentRow, platesNeeded, isLast):
    organiseArr = []
    # Checks if theres more plates than needed in the row
    if platesNeeded < len(currentRow):
        currentRow = currentRow[:platesNeeded]

    sortedArr = sorted(currentRow)

    if isLast:
        # Just add all left over
        highestNum = currentRow[len(currentRow) - 1]

    elif sortedArr[]

    else:
        # Sorts array

        # Highest number is the last index
        highestNum = sortedArr[len(currentRow) - 1]

    # Finds the highest index and sum to it in the original row
    idxHighest = currentRow.index(highestNum)
    sumToHighest = sum(currentRow[0:idxHighest + 1])

    organiseArr.append(idxHighest)
    organiseArr.append(highestNum)
    organiseArr.append(sumToHighest)

    return organiseArr


# Main starts here:
testCases = int(input())

for i in range(testCases):
    total  = 0

    platesBeauty = []
    numStacks, platesInStack, neededPlates = list(map(int, input().split(" ")))
    for j in range(numStacks):
        platesBeauty.append(list(map(int, input().split())))

    numPlates = neededPlates
    isLast = False
    for k in range(len(platesBeauty)):
        if k == (numStacks - 1):
            isLast = True

        checkedRow = rowChecker(platesBeauty[k], numPlates, isLast)

        numPlates -= checkedRow[0] + 1
        total += checkedRow[2]
        if numPlates == 0:
            break


    print("Case #{}: {}".format(i, total))





