# CCC 15 J5 - Pi Day
# Tissan Kugathas
# February 24 2020

n = int(input())
k = int(input())


def pie(pieces, people, minimum):
    total = 0
    if people/pieces == minimum:
        return 1
    elif people == 1:
        return 1
    else:
        times = (pieces//people)
        for i in range(minimum, times):
            total += pie(pieces-i, people-1, i)
        return total


if 1 <= n <= 250 and 1 <= k <= n:
    print(pie(n, k, 1))
