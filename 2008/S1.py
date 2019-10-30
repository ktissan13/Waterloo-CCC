# CCC 2008 S1 - It's Cold Here
# Tissan Kugathas
# ICS4U0
# September 15 2019

city = []
city_temp = []
loop = True
city_num = 0

while loop:
    if city_num <= 10000:
        user_input = input()
        input_split = user_input.split()
        current_city = input_split[0]
        if len(current_city) < 256:
            if -273 <= int(input_split[1]) <= 200:
                city.append(input_split[0])
                city_temp.append(int(input_split[1]))
                if city[city_num] == 'Waterloo':
                    loop = False
                else:
                    city_num += 1
        
coldest = ''
for temp in range(len(city_temp)):
    if coldest == '':
        coldest = city_temp[temp]
    elif coldest > city_temp[temp]:
        coldest = city_temp[temp]

coldest_city_num = city_temp.index(coldest)

print(city[coldest_city_num])

