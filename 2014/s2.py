# CCC '14 S2 - Assigning Partners'
# Tissan Kugathas
# ICS4U0
# December 12 2019

# This is a function to get the dictionary key from a dictionary using the value of a key in a dictionary
def get_key(val):
    # runs each key and value of the group 1 dictionary which hold the first set of input
    for key, value in group1.items():
        # if the value that we are trying the current one are equal, it will return the dictionary key
        if val == value:
            return key

# Initializes the dictionaries
# holds the first set of name inputs
group1 = dict()
# holds the second set of name inputs
group2 = dict()

# asks the users the number of students there are
n = int(input('Enter the N value (1 < N <= 30): '))
# asks the users to enter the first set of names
names1 = input('Enter the first set of the names seprated by spaces: ')
# asks the users to enter the second set of names
names2 = input('Enter the second set of the names seprated by spaces: ')

if 1 < n <= 30:
    # This splits the input by space to get each name
    names1 = names1.split()
    names2 = names2.split()

    # This is a bool to keep track if there any duplicates of names
    no_dupes = True

    if len(names1) == n and len(names2) == n:
        for index in range(n):
            # This for loop checks if there any dupelicate names in each list
            for index1 in range(n):
                if index != index1:
                    if names1[index].isalpha() and names2[index1].isalpha():
                        if names1[index] == names1[index1]:
                            no_dupes = False
                        if names2[index] == names2[index1]:
                            no_dupes = False
                    else:
                        no_dupes = False
    else:
        no_dupes = False
        print('You did not enter right number of names when typing in the names')


    if no_dupes == True:
        # This for loop enters all the names to its according dictionaries
        for index in range(n):
            num = str(index + 1)
            group1[num] = names1[index]
            group2[num] = names2[index]
        # this bool keeps track if the group arrangement is good
        perfect_groups = True
        # for loop to go through each key to see it the group arrangements are good
        for num in group1.keys():
            # calls the key function to get the key of the
            key = get_key(group2[num])
            # if the current partners are paired properly or somebody is paired to themselves
            if group1[num] != group2[key] or group1[key] != group2[num] or group1[num] == group2[num] or group1[key] == group2[key]:
                perfect_groups = False
        if perfect_groups:
            print('good')
        else:
            print('bad')
else:
    print('N has to be greater than 1 and it has to be less than or equal to 30')
