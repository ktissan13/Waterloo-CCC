# CCC 06 S2 Attack of the Cipher Text
# Tissan Kugathas
# ICS4U0
# November 5 2019

a = 'THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG'
b = 'UIFARVJDLACSPXOAGPYAKVNQTAPWFSAUIFAMB ZAEPH'
c = 'XFABSFAWFSZACBEAQFPQMFAEPJOHAWFSZACBEAUIJOHTAIBAIB'

space = 32
min = 65
max = 90
period = 46

final = ''
i = 0
for char in b:
    constant = ord(a[i]) - ord(b[i])
    i += 1
    if i > len(b):
        i = 0
    if ord(char) == space:
        if constant > 0:
            new_letter = min
        else:
            new_letter = max
    els
    new_letter = ord(char) + constant
    if not min <= new_letter <= max:
        if min > new_letter and (min-new_letter) != 1 and (min-new_letter) > 0:
            new_letter = min + (min - new_letter)
        elif max < new_letter and (new_letter-max) != 1 and (new_letter-max) > 0:
            new_letter = max - (new_letter-max)
        else:
            new_letter = space
    final += chr(new_letter)

print(final)
print(constant, ord('b'), ord(' '), ord('Q'))
