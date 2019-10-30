# 2014 J1
# Tissan Kugathas
# ICS 3U0
# March 28 2019

angle1 = int(input())
angle2 = int(input())
angle3 = int(input())

TotalAngle = angle1 + angle2 + angle3

if TotalAngle == 180:
    if angle1 == angle2 and angle1 == angle3 and angle2 == angle3:
            print("Equilateral")
    elif angle1 == angle2 and angle1 != angle3:
        print("Isosceles")
    elif angle1 == angle3 and angle1 != angle2:
        print("Isosceles")
    elif angle2 == angle3 and angle1 != angle2:
        print("Isosceles")
    elif angle1 != angle2 and angle1 != angle3 and angle2 != angle3:
        print("Scalene")

else:
    print("Error")
