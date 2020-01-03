# Sum Game S1
# Tissan Kugathas
# ICS4U0
# December 16 2019

N = int(input())

if 1 <= N <= 100000:
    swifts_input = input()
    semaphores_input = input()
    swifts = swifts_input.split()
    semaphores = semaphores_input.split()
    swifts = [int(i) for i in swifts]
    semaphores = [int(i) for i in semaphores]
    if len(swifts) == N and len(semaphores) == N:
        swifts_total =0
        semaphores_total = 0
        k = 0

        for i in range(N):
            swifts_total += swifts[i]
            semaphores_total += semaphores[i]
            if swifts_total == semaphores_total:
                k = i+1

    print(k)
