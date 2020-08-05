'''
Cracking The Coding Interview
'''

def urlify(spacedString, length):
    spaced_list = list(spacedString)
    for i in range(length):
        if spaced_list[i] == " ":
            spaced_list[i] = "%20"

    return "".join(spaced_list)

print(urlify("I am a test", 11))