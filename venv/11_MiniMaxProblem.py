'''
HackerRank Question
'''
def miniMaxSum(arr):
    minSum = 0
    maxSum = 0
    sortedArr = sorted(arr)
    for i in range (1, len(arr)):
        maxSum += sortedArr[i]

    for j in range(0, len(arr) - 1):
        minSum += sortedArr[j]

    return minSum, maxSum

print(miniMaxSum([1,2,3,4,5]))