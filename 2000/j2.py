# J2 2000 9966
# Tissan Kugathas
# ICS4U0
# October 3O 2019

m = int(input())
n = int(input())
final = 0

if 1 <= m <= n <= 32000:
    for num in range(m,n,1):
        string = str(num)
        temp = 0
        backwards = ''
        for elem in reversed(range(len(string))):
            if string[elem] == '1' or string[elem] ==  '8' or string[elem] == '0':
                temp += 1
            if num > 10:
                if string[elem] == '6' or string[elem] == '9':
                    temp += 1
            backwards += string[elem]
        if len(string) == temp and string == backwards:
            final += 1

print(final)
