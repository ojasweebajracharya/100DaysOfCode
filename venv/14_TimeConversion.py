'''
HackerRank: Easy
'''

def timeConversion(s):
    sArr = s.split(":")
    amOrpm = s[-2:]

    if sArr[0] == "12" and amOrpm == "AM":
        sArr[0] = "00"
        return (":".join(sArr))[:-2]
    elif sArr[0] == "12" and amOrpm == "PM":
        return s[:-2]
    elif amOrpm == "AM":
        return s[:-2]
    else:
        sArr[0] = str(int(sArr[0]) + 12)
        return (":".join(sArr))[:-2]


s = input()
print(timeConversion(s))