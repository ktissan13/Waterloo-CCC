# 1996 j2 divisibility by 11
# Tissan Kugathas
# ICS 3U0
# May 31 2019

repeater = int(input())

for current in range(repeater):
    integer = int(input())
    original_int = integer
    status =  True
    while(status):
        integer = integer // 11
        print(integer)
        if integer == 11:
            print("The number", original_int, "is divisible by 11.")
            status = False
        if integer < 11:
            print("The number", original_int, "is not divisible by 11.")
            status = False
