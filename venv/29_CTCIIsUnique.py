'''
Cracking The Coding Interview #1.1
'''

def isUnique(word):

    alphabet = list(map(chr, range(97, 123)))

    for letter in word:
        if letter in alphabet:
            alphabet.remove(letter)
        else:
            return False

    return True

print(isUnique("cat"))