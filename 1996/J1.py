# 1996 J1 Deficient, Perfect, and Abundant
# Tissan Kugathas
# ICS 3U0
# May 31 2019

repeat = int(input())


for current in range(repeat):
    integer = int(input())
    if 1 <= integer <= 32500:
        total = 0
        for multiplier in range(1,(integer//2)+1):
            if integer % multiplier == 0:
                total += multiplier
        if total == integer:
            print(integer, "is a perfect number.")
        elif total < integer:
            print(integer, "is a deficient number.")
        elif total > integer:
            print(integer, "is an abundant number.")
