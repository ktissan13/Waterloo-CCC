# CCC S2 01 Sprials
# Tissan Kugathas
# ICS4U0
# September 18 2019

import math

numbers = []
chart = []

x = int(input())
y = int(input())

if x < 100:
    if y < 100:
        for number in range(x, y+1, 1):
            numbers.append(number)
        colum_num = round(math.sqrt(len(numbers))) + 1
        row_num = round(math.sqrt(len(numbers)))
        total_square = 0
        for colum in range(colum_num):
            chart.append([])
            for row in range(row_num):
                chart[colum].append([])
                total_square += 1
        skip = total_square - len(numbers)
        colum = 0
        min_c = 0
        min_r = -1
        row = 0
        d = False
        u = False
        r = True
        l = False
        status = True
        for skips in range(skip):
            chart[colum][row] = ' '
            row += 1
        while status:
            if r and len(numbers) > 0:
                chart[colum][row] = numbers[-1]
                numbers.pop()
                row += 1
                if row == row_num:
                    row -= 1
                    colum += 1
                    d = True
                    r = False
                    row_num -= 1
            elif d and len(numbers) > 0:
                chart[colum][row] = numbers[-1]
                numbers.pop()
                colum += 1
                if colum == colum_num:
                    colum -= 1
                    row -= 1
                    d = False
                    l = True
                    colum_num -= 1
            elif l and len(numbers) > 0:
                chart[colum][row] = numbers[-1]
                numbers.pop()
                row -= 1
                if row == min_r:
                    row += 1
                    colum -= 1
                    u = True
                    l = False
                    min_r += 1
            elif u and len(numbers) > 0:
                chart[colum][row] = numbers[-1]
                numbers.pop()
                colum -= 1
                if colum == min_c:
                    row += 1
                    colum += 1
                    r = True
                    u = False
            else:
                status = False

        for colum in chart:
            final = ''
            for row in colum:
                final += str(row)
            print(final)
