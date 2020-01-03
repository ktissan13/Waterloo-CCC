# Problem J2 2006
# Tissan Kugathas
# ICS3U0
# April 15 2019

m = int(input("Enter m: "))
n = int(input("Enter n: "))
sum_to_10 = 0

if (1 <= m <= 1000) and (1 <= n <= 1000):
    for current_m in range(m+1):
        for current_n in range(n, 0, -1):
            sum = current_m + current_n
            if sum == 10:
                sum_to_10 += 1
    print(sum_to_10)


else:
    print("Error!")
