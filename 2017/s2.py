# CCC 17 S2 - High Tide, Low Tide
# Tissan Kugathas
# ICS4U0
# December 13 2019

low_tides = []
final = ''
status  = True

N = int(input())

if 1 <= N <= 100:
    tide = input()

    high_tides = tide.split()
    high_tides = [int(i) for i in high_tides]
    high_tides.sort()

    for tide in high_tides:
        if tide > 1000000:
            status = False

    if N%2 == 0:
        split_num = N//2
    else:
        split_num = (N//2)+1
            
    if status:
        for index in range(split_num):
            low_tides.append(high_tides[0])
            high_tides.pop(0)

        for index in range(N):
            if not index%2 == 0 and high_tides:
                final += str(high_tides[0])
                high_tides.pop(0)
            elif low_tides:
                final += str(low_tides[-1])
                low_tides.pop()
            final += ' '

        print(final)
