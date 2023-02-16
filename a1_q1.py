'''
Python Assignment 1
Name: Haani Syed
Date: 2023-01-19
'''

import random #importing random
random_number_1 = random.randint(0,100) #random number 1 (Smaller number)
random_number_2 = random.randint(0,100)#random number 2 (Larger Number)
print(random_number_1, random_number_2)
if random_number_1 > random_number_2:
    tmp = random_number_1
    random_number_1 = random_number_2
    random_number_2 = tmp  # this block of code ensures that random_number_2 is the larger number
distance = (random_number_2 - random_number_1)
while distance > 50 or distance < 10:
    print('This pair of integers is invalid')
    if distance < 10:
        random_number_2 = random_number_2 * 2
    if distance > 50: #if its too far apart means distance is greater than 10
        if random_number_2 % 3 != 0:
            random_number_2 = (random_number_2 // 3) + 1
        else:
            random_number_2 = random_number_2 // 3

    print(random_number_1, random_number_2)
    if random_number_1 > random_number_2:
        tmp = random_number_1
        random_number_1 = random_number_2
        random_number_2 = tmp #this block of code ensures that random_number_2 is the larger number
        distance = (random_number_2 - random_number_1)


print('This pair of integers is valid')
for num in range(random_number_1, random_number_2):
    flag = False
    if num % 5 == 0:
        flag = True
        print('apple', end=' ')
    if num % 7 == 0:
        flag = True
        print('pen', end=' ')
    if '3' in str(num):
        flag = True
        print('pineapple', end=' ')
    if flag == False:
        print(num)
    print()




