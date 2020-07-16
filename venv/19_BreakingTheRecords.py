'''
HackerRank Question : Easy
'''

def breakingRecords(scores):
    min = scores[0]
    max = scores[0]
    countMin = 0
    countMax = 0
    for game,score in enumerate(scores):
        if score < min:
            min = scores[game]
            countMin += 1
        elif score > max:
            max = scores[game]
            countMax += 1

        print(game, score, min, max, countMin, countMax)
    return countMax, countMin

