# CCC 2019 J2 Time to Decompress
# Tissan Kugathas
# ICS 3U0
# June 10th 2019

def repeater(times, string):
    final_string = ''
    for current_number in range(times):
        final_string += string
    print(final_string)
    
lines = int(input())
inputs = []

for current_input in range(lines):
    inputs.append(input())

for current_input in inputs:
    input_values = current_input.split(" ")
    repeater(int(input_values[0]),input_values[1])
    
