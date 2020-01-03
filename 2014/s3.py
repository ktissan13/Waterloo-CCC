# CCC '14 S3 - The Geneva Confection'
# Tissan Kugathas
# ICS4U0
# December 12 2019

# A dictionary to store all of the test cases
testcase = dict()

# asks the user for the number of test cases
T = int(input("Enter the number of test cases: "))

# a bool variable to keep track of the all the inputs qualify
status = True

if 1 <= T <= 10:

    # for loop to get the inputs from the user
    for test in range(T):
        testcase[str(test+1)] = dict()
        # asks the user numbers of carts
        N = int(input('Enter the number of carts in testcase #{}: '.format(test+1)))
        testcase[str(test+1)]['N'] = N
        # checks if the input meets the minimum and maximum value
        if 1 <= N <= 100000:
            for i in range(N):
                cart_num = int(input('Enter the cart number: '))
                if 1 <= cart_num <= N:
                    testcase[str(test+1)][str(i+1)] = cart_num
                else:
                    # sets status false due to inputs not being valid
                    status = False
        else:
            # sets status false due to inputs not being valid
            status = False

    if status:
        # goes through each test case
        for test in range(T):
            # initializes the mountain dictionary
            mountain = {}
            # sets order number to 1
            order = 1
            # gets the N value for the current test case
            N = testcase[str(test+1)]['N']
            # puts the carts in order in on top of the mountain
            for index in range(N,0,-1):
                mountain[str(index)] = testcase[str(test+1)][str(order)]
                order += 1
            # initializes the branch dictionary
            branch = {}
            # sets the current number of the cart that needs be in the lake
            nextCart = 1
            # sets the first cart number in the mountain
            mountainCart = 1
            # sets the branchCart to 0 as there is no cart there
            branchCart = 1
            branchCartList = []
            # bool function to see if the ingred are good
            taste = True

            # while loop to run until it goes through all the carts
            while taste and mountainCart <= N:
                # if the current mountain cart is the next cart in the lake, it will go into the lake
                if mountain[str(mountainCart)] == nextCart and mountainCart <= N:
                    nextCart += 1
                    mountainCart += 1
                # if the current branch cart is the next cart to go into the lake, it will go into the lake
                elif len(branch) > 0 and branch[str(branchCartList[-1])] == nextCart:
                    nextCart += 1
                    branchCartList.pop()
                # if the mountain cart should go to the branch, it will go into the branch
                elif mountainCart < N:
                    branchCart += 1
                    branchCartList.append(branchCart)
                    branch[str(branchCart)] = mountain[str(mountainCart)]
                    mountainCart += 1
                # if the code went through all the carts and not all of them went to lake, then taste will false
                else:
                    taste = False

            # if taste is true then it will return 'Y'
            if taste:
                print("Y")
            # else it will return 'N'
            else:
                print("N")
