'''
HackerRank: Easy
'''


def migratoryBirds(arr):
    birdDict = {"1":0, "2":0, "3":0, "4":0, "5":0}
    for i in range(len(arr)):
        birdDict[arr[i]] += 1

    orderedValues = sorted(birdDict.values(), reverse = True)
    key_list = list(birdDict.keys())
    val_list = list(birdDict.values())

    return(key_list[val_list.index(orderedValues[0])])

# if __name__ == '__main__':
#     file = open("hiddentestfor22.txt","r")
#     arr = (file.readline()).split()
#     print(migratoryBirds(arr))


