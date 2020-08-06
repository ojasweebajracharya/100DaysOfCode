'''
Cracking The Coding Interview #1.6
'''
import re


def string_compression(longstring):
    shortstring = []
    counter = 1
    for i in range(len(longstring)):
        if i == (len(longstring) - 1):
            shortstring.append([longstring[i], counter])
        elif longstring[i] == longstring[i+1]:
            counter += 1
        else:
            shortstring.append([longstring[i], counter])
            counter = 1

    strlist = "".join(list(map(str, shortstring)))
    final = "".join(re.split("[^a-zA-Z0-9*]", strlist))
    return final


print(string_compression("aabcccccaaa"))
