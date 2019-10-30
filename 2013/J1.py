# Waterloo 2013 J1 Next in line
# Tissan Kugathas
# ICS 3U0
# June 10th 2019

youngest = int(input())

if 0 <= youngest <= 50:
    middle = int(input())
    if youngest <= middle <= 50:
        difference = middle - youngest
        print(middle + difference)

else:
    print("Invalid Input, Youngest has to greater than or equal to 0 and less than or equal to 50")
