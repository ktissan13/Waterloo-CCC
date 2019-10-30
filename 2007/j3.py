# J3 Deal or No Deal Calculator
# Tissan Kugathas
# ICS 3U0
# May 16 2019

briefcase = [100,500,1000,5000,10000,25000,50000,100000,500000,1000000]
total = 0 
status = True
opened = []

while(status):
    case = int(input())
    if 1 < case < 11:
        if not case in opened:
            opened.append(case)
    elif 1 > case:
        print("Input has to be greater than 0")
    if case > 10:
        offer = case
        status = False

for money in briefcase:
    if (briefcase.index(money)+1) in opened:
        total += 0
    else:
        total += money

average = total/(10-len(opened))

if offer > average:
    print("deal")
else:
    print("no deal")
