'''
Python 121 Assignment 1
Name: Haani Syed
Date: 2023-01-19
'''
import random
file = open('myspace_profiles.txt', 'a') #write the file with append mode
file.write('Haani' + '\n')
file.write('18' +  '\n')
file.write('blue' +  '\n')
file.write('-' +  '\n')
person = input('Enter your name: ' +  '\n')
file.write(person +  '\n')
age = str(random.randint(18,22))
file.write(age +  '\n')
color = random.randint(0, 5)
colors = {0: 'green', 1: 'red', 2: 'yellow', 3: 'pink', 4: 'blue', 5: 'orange'}
file.write(colors[color] +  '\n')
file.write('-' +  '\n')
file.close()
file = open('myspace_profiles.txt', 'r')
content = file.readlines()

print(content)


