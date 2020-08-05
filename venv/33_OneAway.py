'''
Cracking The Coding Interview
'''

def oneAway(string_a, string_b):
    list_a = list(string_a)
    list_b = list(string_b)

    count = 0

    for i in list_b:
        if i in list_a:
            list_a.remove(i)
        else:
            count += 1


    if count <= 1:
        return True
    else:
        return False


print(oneAway("pale","ple"))
print(oneAway("pale","bake"))