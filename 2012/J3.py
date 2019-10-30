# Waterloo CCC 2012 J3 Icon Scaling
# Tissan Kugathas
# ICS 3U0
# June 10th 2019

def print_strings(first,second,third,k):
    for line in range(k):
        string = ''
        for current in range(k):
            string += first
        for current in range(k):
            string += second
        for current in range(k):
            string += third
        print(string)    

k = int(input())

if k < 25:
    print_strings('*','x','*',k)
    print_strings(' ','x','x',k)
    print_strings('*',' ','*',k)
