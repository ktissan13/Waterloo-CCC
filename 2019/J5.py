# CCC 19 J5 Rule of Three
# Tissan Kugathas
# September 30 2019


sub = []

for current in range(3):
    current_input = input()
    temp = current_input.split()
    sub.append([])
    sub[current].append([])
    sub[current]=temp[0]
    sub[current].append(temp[1])

print(sub)
    
