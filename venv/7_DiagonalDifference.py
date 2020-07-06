'''
HackerRank Question
'''


def diagonalDifference(arr):
    # Write your code here
        # i = rows
    # j = column
    j = 0
    diag1 = []
    diag2 = []
    k = len(arr) - 1
    for i in range(len(arr)):

        diag1.append(arr[i][j])
        diag2.append(arr[k][j])
        j += 1
        k -= 1

    result = abs(sum(diag1) - sum(diag2))
    return result


if __name__ == '__main__':

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
    print(result)


