# 00 j3 slot machine
# Tissan Kugathas
# ICS4U0
# October 31 2019


win = [35,100,10]
prize = [30,60,9]

#m = 48
m_played = 0

m = int(input())
a = int(input())
b = int(input())
c = int(input())

if 0 <= a < 35 and 0 <= b < 100 and 0 <= c < 10:
    played = [a,b,c]

if 1 <= m <= 1000:
    while m > 0:
        for i in range(3):
            if m > 0:
                m_played += 1
                played[i] += 1
                m -= 1
                if played[i] == win[i]:
                    m += prize[i]
                    played[i] = 0


print('Martha plays {} times before going broke.'.format(m_played))
