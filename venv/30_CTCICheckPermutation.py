'''
Cracking the Coding Interview #1.2
'''

def checkPermutations(string_a, string_b):
    array_a = list(string_a)
    array_b = list(string_b)

    if sorted(string_a) == sorted(string_b):
        return True

    for letter in array_b:
        if letter in array_a:
            array_a.remove(letter)
        else:
            return False
    return True

print(checkPermutations("weather", "wet"))