# CCC 11 S2 - Multiple Choice
# Tissan Kugathas
# ICS4U0
# January 16 2020

answers = []
student = []
correct = 0

n = int(input())

if 0 < n < 10000:
    for ans in range(n):
        answers.append(input())
    for stu in range(n):
        student.append(input())
    for index in range(n):
        if answers[index] == student[index]:
            correct += 1

print(correct)
