# 2000 J1 Calender
# Tissan Kugathas
# ICS 3U0
# May 29 2019

# ERROR function which runs if the user input an error
def ERROR(which_input):
    # This option is for when the user input of days of the week is invalid
    if which_input == 1:
        print("Invalid input, the day of the week has to be between 1 and 7")
    # This option is for when the user input of days of the month is invalid
    elif which_input == 2:
        print("Invalid input,  the days of the month has to between 28 and 31")
    
    
def create_calendar(day_of_the_week, days):
    print("%-2s %3s %3s %3s %3s %3s %3s"%('Sun', 'Mon', 'Tue', 'Wed', 'Thr', 'Fri', 'Sat'))
    month = True
    first_week = True
    day = 1
    while(month):
        for index_of_day in range(7):
            if first_week:
                if index_of_day < day_of_the_week-1:
                    if index_of_day == 0:
                        print("%2s"%(""), end="")
                    else:
                        print("%3s"%(""), end="")
                else:
                    if index_of_day == 0:
                        print("%2s"%(day), end="")
                        day += 1
                    else:
                        print("%3s"%(day), end="")
                        day += 1
                if index_of_day == 6:
                    print("\n", end="")
                    first_week = False
            elif day > days:
                month = False
                break
            else:
                if index_of_day == 0:
                        print("%2s"%(day), end="")
                        day += 1
                else:
                    print("%3s"%(day), end="")
                    day += 1
                if index_of_day == 6:
                    print("\n", end="")

# This asks the user the day of the week that the month start and the numbers of days of the month split with a space
user_input = input()

# This seprates the two integers needed into a list
user_inputs = user_input.split(" ")

# this gets the day of the week
day_of_the_week = int(user_inputs[0])

# this gets the number of days of the month
days = int(user_inputs[1])

# Check if the day of the week is within the range of 1 to 7
if 1 <= day_of_the_week <= 7:
    # Check if the days is within the range of 28 to 31
    if 28 <= days <= 31:
        # Call the create Calendar function
        create_calendar(day_of_the_week, days)
        print()
    else:
        # If it false then it will run ERROR function and run the 2 option
        ERROR(2)
else:
    # If it is false then it will run ERROR function and run the 1 option
    ERROR(1)
