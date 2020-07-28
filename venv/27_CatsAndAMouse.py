'''
HackerRank: Easy
'''

# x = Cat A position
# y = Cat B position
# z = Mouse position

def bigger(position, z):
    if position > z:
        ans = position - z
    else:
        ans = z - position

    return ans

def catAndMouse(x, y, z):

    diffx = bigger(x, z)
    diffy = bigger(y, z)

    if diffx == diffy:
        return "Mouse C"
    elif diffx > diffy:
        return "Cat B"
    else:
        return "Cat A"

print(catAndMouse(1,2,3))

