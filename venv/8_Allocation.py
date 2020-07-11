'''
KickStart 2020 Round A Question Q1
'''

# cases = int(input())
# buyHouses = [0] * cases
# for i in range(cases):
#     numHouses, budget = input().split(" ")
#     costs = list(map(int, input().split(" ")))
#     budget = int(budget)
#
#     costs = sorted(costs)
#     for cost in costs:
#         budget -= int(cost)
#         if budget < 0:
#             break
#         else:
#             buyHouses[i] += 1
#
# for i in range(len(buyHouses)):
#     print(f"Case #{i + 1}: {buyHouses[i]}")

cases = int(input())
buyHouses = 0
for i in range(cases):
    numHouses, budget = input().split(" ")
    costs = list(map(int, input().split(" ")))
    budget = int(budget)

    costs = sorted(costs)
    for cost in costs:
        budget -= int(cost)
        if budget < 0:
            break
        else:
            buyHouses += 1

    print(f"Case #{i + 1}: {buyHouses}")
    buyHouses = 0


    # sort low to high
    # take away from budget smallest, if negative return buyHouses


