# 00 j3 slot machine
# Tissan Kugathas
# ICS4U0
# October 31 2019

played = [3,10,4]
win = [35,100,10]
prize = [30,60,9]

m = 48
m_played = 0

for i in range(3):
    if m>0:
        loop = True
        while loop:
            m_played += 1
            played[i] += 1
            m -= 1
            if played[i] == win[i]:
                print(m)
                print(m_played)
                m += prize[i]
                played[i] = 0
                loop = False
                print(m)
            elif m == 0:
                loop = False

print(m_played)
