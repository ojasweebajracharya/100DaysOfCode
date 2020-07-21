'''
HackerRank: Easy
'''
# k = item Anna didn't eat
# b = amount Anna contributed

def bonAppetit(bill, k, b):
    bill.pop(k)
    count = 0
    for i in bill:
        count += i

    pay = b - (count // 2)

    if pay == 0:
        print("Bon Appetit")
        return "Bon Appetit"
    else:
        print(pay)
        return pay


bonAppetit([3,10,2,9],1,12)
