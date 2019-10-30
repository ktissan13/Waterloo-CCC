# Waterloo CCC 2014 J3 Double Dice
# Tissan Kugathas
# ICS 3U0
# June 10th 2019

rounds = int(input())
Antonia_points = 100
David_points = 100

if 1 <= rounds <= 15:
    for current_round in range(rounds):
        user_input = str(input())
        points = user_input.split(' ')
        if int(points[0]) < int(points[1]):
            Antonia_points -= int(points[1])
        elif int(points[0]) > int(points[1]):
            David_points -= int(points[0])
    print(Antonia_points)
    print(David_points)
