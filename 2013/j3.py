# CCC 13 J3 - From 1987 to 2013
# Tissan Kugathas
# ICS4U0
# Janurary 15 2020

y = int(input())
y += 1

if 0 <= y <= 10000:
    distinct = False
    found = False
    while not distinct:
        temp = []
        string = str(y)
        for char in string:
            if string.count(char) > 1:
                break
            elif char == string[len(string)-1]:
                found = True
        if found:
            print(y)
            distinct = True
        else:
            y += 1
