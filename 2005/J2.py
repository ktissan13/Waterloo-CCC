# Problem J2 2005
# Tissan Kugathas
# ICS 3U0
# April 15 2019

lower_limit = int(input())
upper_limit = int(input())
RSA_NUMBER = 0;

for current_number in range(lower_limit, upper_limit+1):
    equal_divisor = 0;
    for divisor in range(1, current_number +1):
        if current_number%divisor == 0:
            equal_divisor += 1
    if equal_divisor == 4:
        RSA_NUMBER += 1
print("The number of RSA numbers between",lower_limit, "and", upper_limit, "is", RSA_NUMBER)
