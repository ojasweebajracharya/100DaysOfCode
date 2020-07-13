def countApplesAndOranges(s, t, a, b, apples, oranges):
    appleCount = 0
    orangeCount = 0

    for i in apples:
        sumApple = a + i
        if sumApple in range(s, t+1):
            appleCount += 1

    for j in oranges:
        sumOrange = b + j
        if sumOrange in range(s, t+1):
            orangeCount += 1

    print(appleCount)
    print(orangeCount)
    return appleCount, orangeCount

