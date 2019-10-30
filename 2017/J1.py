# CCC 17 J1 Quadrant Selection
# Tissan Kugathas
# ICS4U0
# October 1 2019

x = int(input())
y = int(input())

if -1000<=x<=1000 and x != 0:
    if -1000 <= y <= 1000 and y != 0:
        if x<0:
            if y>0:
                print(2)
            elif y<0:
                print(3)
        if x>0:
            if y>0:
                print(1)
            if y<0:
                print(4)
