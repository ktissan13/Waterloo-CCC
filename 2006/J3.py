# J3 Cell Phone Messaging
# Tissan Kugathas
# ICS 3U0
# May 15 2019

text = []
status = True
_1_press_letters = ['a', 'd', 'g', 'j', 'm', 'p', 't', 'w']
_2_press_letters = ['b', 'e', 'h', 'k', 'n', 'q', 'u', 'x']
_3_press_letters = ['c', 'f', 'i', 'l', 'o', 'r', 'v', 'y']
_4_press_letters = ['s', 'z']

while (status):
    current_text = input("Enter text: ")
    if current_text.lower() == "halt":
        status = False
    else:
        text.append(current_text.lower())


last_letter = ''


for string in text:
    seconds = 0
    last_letter = ''
    last_index = ''
    for letter in string:
        if letter == last_letter:
            seconds += 2
            different_letter = False
        else:
            different_letter = True
        if letter in _1_press_letters:
            seconds += 1
            if different_letter:
                if _1_press_letters.index(letter) == last_index:
                    seconds += 2
            last_index = _1_press_letters.index(letter)
        if letter in _2_press_letters:
            seconds += 2
            if different_letter:
                if _2_press_letters.index(letter) == last_index:
                    seconds += 2
            last_index = _2_press_letters.index(letter)
        if letter in _3_press_letters:
            seconds += 3
            if different_letter:
                if _3_press_letters.index(letter) == last_index:
                    seconds += 2
            last_index = _3_press_letters.index(letter)
        if letter in _4_press_letters:
            seconds += 4
            if different_letter:
                if _4_press_letters.index(letter) == last_index:
                    seconds += 2
            last_index = _4_press_letters.index(letter)
        last_letter = letter
    print(seconds)
