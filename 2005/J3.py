# J3 Returning Home 2005
# Tissan Kugathas
# ICS 3U0
# May 14 2019

status = True
turns = []
streets = []

while (status):
    current_turn = input()
    current_street = input()
    turns.append(current_turn.upper())
    if current_street.upper() == "SCHOOL":
        streets.append("HOME")
        status = False
    else:
        streets.append(current_street.upper())
street = len(streets)-2

for turn in reversed(turns):
    if turn == "L":
        if street == -1:
            print("Turn RIGHT into your HOME.")
        else:
            print("Turn RIGHT onto", streets[street], "street.")
    if turn == "R":
        if street == -1:
            print("Turn LEFT into your HOME.")
        else:
            print("Turn LEFT onto", streets[street], "street.")
    street -= 1
