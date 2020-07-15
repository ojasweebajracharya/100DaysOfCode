def kangaroo(x1, v1, x2, v2):
    if v2 >= v1 and x2 >= x1:
        print("No")
        return "NO"
    else:
        if v1 != v2 and (x2-x1)%(v2-v1) == 0:
            return "YES"
        else:
            return "NO"
kangaroo(0,2,5,3)