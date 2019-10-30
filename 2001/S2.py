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
        for number in range(x,y+1,1):
            numbers.append(number)
        colum_num = round(math.sqrt(len(numbers))) + 1
        total_square = 0
        for colum in range(colum_num):
            chart.append([])
            for row in range(round(math.sqrt(len(numbers)))):
                chart[colum].append([])
                total_square += 1
        skip = total_square - len(numbers)
        current_square = 0
        for colum in range(len(chart)):
            for row in range(len(chart[colum])):
                if current_square < skip:
                    chart[colum][row] = ' '
                else:
                    index = (len(numbers)-(current_square-skip+1))
                    chart[colum][row] = numbers[index]
                current_square += 1
        for colum in chart:
            print(colum)
        
