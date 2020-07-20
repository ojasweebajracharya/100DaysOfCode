'''
HackerRank: Easy
'''
def dayAndMonth(months):
    count = 1  # totaldays
    i = 1  # month counter
    while count + months[i] < 256:
        count += months[i]
        i += 1

    day = 256 - count

    if day < 10:
        day = leadingZero(day)

    if i < 10:
        i = leadingZero(i)

    return day, i

def leadingZero(num):
    num_str = str(num)
    zero_filled = num_str.zfill(2)
    return zero_filled


def dayOfProgrammer(year):
    # Get 256th day
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    leapMonths = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    months1918Russia = [31, 15, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    leap = False

    if year == 1918:
        day, month = dayAndMonth(months1918Russia)
    else:

        if year < 1919:
            if year % 4 == 0:
                leap = True

        else:
            if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
                leap = True

        if leap:
            day, month = dayAndMonth(leapMonths)
        else:
            day, month = dayAndMonth(months)


    return (f"{day}.{month}.{year}")

print(dayOfProgrammer(1918))