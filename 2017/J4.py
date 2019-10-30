# CCC 17 J4 Favourite Times
# Tissan Kugathas
# ICS4U0
# October 2 2019
        
                
        

D = int(input())

if 0 <= D <= 1000000000:
    current_time = 1200
    seq = 0
    for current in range(D):
        time = str(current_time)
        digits = len(time)
        if digits == 3:
            if (int(time[2])-int(time[1])) == (int(digits[1])-int(digits[0])):
                self.seq += 1
                end_digits = digits[2]+digits[1]
        elif digits == 4:
            if (int(digits[3])-int(digits[2]))==(int(digits[2])-int(digits[1])) and (int(digits[2])-int(digits[1]))==(int(digits[1])-int(digits[0])):
                self.seq += 1
        current_time += 1
        if current_time > 1259:
            current_time = 100
                
    print(seq)
    
