'''
HackerRank: Easy
'''

def getMoneySpent(keyboards, drives, b):
    highest = 0

    drives = sorted(drives)
    keyboards = sorted(keyboards, reverse=True)

    for i in keyboards:
        for j in drives:
            total = j + i
            if total <= b and total >= highest:
                highest = total

    if highest == 0:
        return -1
    else:
        return highest


print(getMoneySpent([4],[5],5))
