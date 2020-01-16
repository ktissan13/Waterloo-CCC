# CCC 08 j3 - GPS Text Entry
# Tissan Kugathas
# ICS4U0
# January 16 2020

keyboard = [['A', 'B', 'C', 'D', 'E', 'F'], ['G', 'H', 'I', 'J', 'K', 'L'], [
    'M', 'N', 'O', 'P', 'Q', 'R'], ['S', 'T', 'U', 'V', 'W', 'X'], ['Y', 'Z', ' ', '-', '.', 'ENTER']]

destination = input()
destination = destination.upper()

index = 0
moved = 0
cursor = [0, 0]

while index < len(destination):

    for colum in range(len(keyboard)):
        if destination[index] in keyboard[colum]:
            letter_column = colum

    for row in range(len(keyboard[letter_column])):
        if keyboard[letter_column][row] == destination[index]:
            letter_row = row
    moved += abs(cursor[0] - letter_column) + abs(cursor[1] - letter_row)
    cursor = [letter_column, letter_row]
    index += 1

letter_column = 4
letter_row = 5
moved += abs(cursor[0] - letter_column) + abs(cursor[1] - letter_row)

print(moved)
