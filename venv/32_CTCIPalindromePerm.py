'''
Cracking The Coding Interview
'''

def palindrome_perm(checkword):
    letter_dict = dict()
    checklist = list(checkword.upper())

    for i in range(len(checklist)):
        letter_dict[checklist[i]] += 1

    counter = 0

    for j in letter_dict.values():
        if j & 2 != 0:
            counter += 1

    if counter == 0 or counter == 1:
        return True
    else:
        return False
