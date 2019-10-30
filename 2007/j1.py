# CCC 07 j1 Who is the middle
# Tissan Kugathas
# October 5 2019

a = int(input())
b = int(input())
c = int(input())

if b > a and a > c:
    print(a)
elif a > b and b > c:
    print(b)
elif c > a and a > b:
    print(a)
elif c > b and b > a:
    print(b)
elif a > c and c > b:
    print(c)
elif b >c and c > a:
    print(c) 
