# CCC '14 S3 - The Geneva Confection'
# Tissan Kugathas
# ICS4U0
# December 12 2019

# asks the user for the number of test cases
testcase = int(input("Enter the number of test cases: "))


if 1 <= testcase <= 10:
    # for loop to get the inputs from the user
    for test in range(testcase):
        # asks the user numbers of carts
        total = int(input('Enter the number of carts in testcase #{}: '.format(test+1)))
        if 1 <= total <= 100000:
            # initializes the mountain
            mountain = []
            # adds the cart to the mountain
            for x in range(total):
                mountain.append(int(input('Enter cart number: ')))

            # initializes the branch list
            branch = []

            # keeps in track if the moutain and branch are empty
            empty = False
            # check if all the ingredients are good/yummy
            taste = False
            # the current cart that needs to be in the lake
            current = 1

            # runs a while loop until the carts went in
            while not empty:

                # if the both mountain and branch are empty them it will end the while loop and set taste to True
                if not mountain and not branch:
                    empty = True
                    taste = True
                # if mountain is empty and branch is not and last cart in branch is not the cart that should go in the lake then end the while loop
                elif not mountain and branch and branch[-1] != current:
                    empty = True
                # if there carts in the mountain and the last cart is next cart to go into the lake, it will go into the lake
                elif mountain and mountain[-1] == current:
                    mountain.pop()
                    current += 1
                # if there are cart in branch and the last cart is next cart go to the lake then it will go to the lake
                elif branch and branch[-1] == current:
                    branch.pop()
                    current += 1
                # add the mountain cart to the branch
                else:
                    # adds the mountain cart to the branch and remove that cart from
                    branch.append(mountain.pop())

            # if taste is true then it will return 'Y'
            if taste:
                print("Y")
            # else it will return 'N'
            else:
                print("N")
