# J2 2000 9966
# Tissan Kugathas
# ICS4U0
# October 3O 2019

m = 1
n = 100
final = 0

if 1 <= m <= n <= 32000:
    for num in range(m,n,1):
        string = str(num)
        temp = 0
        for elem in string:
            if elem == '1' or elem == '8' or elem == '6' or elem == '9' or elem == '0':
                temp += 1
        if len(string) == temp:
            final += 1

print(final)
