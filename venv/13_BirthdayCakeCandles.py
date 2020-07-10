def birthdayCakeCandles(ar):
    sortArr = sorted(ar, reverse = True)
    dictArr = dict()

    for i in range(len(ar)):
        if sortArr[i] in dictArr:
            dictArr[sortArr[i]] += 1
        else:
            dictArr[sortArr[i]] = 1

    return dictArr[sortArr[0]]

    # Runtime error for 2 tests due to large num of inputs
    # counter = 0
    # index = 0
    # current = 0
    # if len(ar) == 1:
    #     return 1
    # elif len(ar) == 0:
    #     return 0
    # else:
    #     while sortArr[current] == sortArr[0]:
    #         counter += 1
    #         current += 1
    #
    #     return counter


