'''
HackerRank: Easy
'''
def divisibleSumPairs(n, k, ar):
    count = 0
    for i in range(n-1):
        for j in range(1, n):
            if i < j:
                divisible = (ar[i] + ar[j]) % k
                if divisible == 0:
                    count += 1

    return count


print(divisibleSumPairs(6,3,[1,3,2,6,1,2]))