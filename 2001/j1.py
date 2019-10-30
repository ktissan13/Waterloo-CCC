## CCC 01 J1 Dressing Up
# Tissan Kugathas
# ICS4U0
# October 4 2019

H = int(input())
lt = 0
gt = (H*2)-1
flip = False

for colum in range(H):
    temp=''
    for row in range(H*2):
        if row > lt and row < gt:
            temp += ' '
        else:
            temp += '*'
    print(temp)
    if not flip:
            lt += 2
            gt -= 2
            if lt > H-2:
                flip = True
    else:
        lt -= 2
        gt += 2
        
