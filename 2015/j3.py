# CCCHK 15 J3 Queens can't attack me
# Tissan Kugathas
# October 1 2019


user_input = input()
temp = user_input.split()
N = int(temp[0])
M = int(temp[1])
board = []

ffor colum in range(N):
    board.append([])
    for row in range(N):
        board[colum].append([])

for queen in range(M):
    user_input = input()
    temp = user_input.split()
    if 1 <= int(temp[0]) <= N and 1 <= int(temp[1]) <= N:
        x = int(temp[0])-1
        y = int(temp[1])-1
        for current_x in range(x-1,x+2,1):
            for current_y in range(y-1,y+2,1):
                board[current_x][current_y] = 'X'
            
            

for colum in board:
    print(colum)
