# fruit = 'banana'
# letter = fruit[1:4]
# print(letter)

# print(len(fruit))
# print(fruit[len(fruit)-1])
# print(fruit[-1])

"""
Traversal through a string with a loop
"""
# fruit = 'banana'

# for letter in fruit:
#     print(letter)

# index = 0
# while index < len(fruit):
#     print(fruit[index])
#     index += 1

# index = len(fruit) - 1
# while index >= 0:
#     print(fruit[index])
#     index -= 1

# index = -1
# while abs(index) <= len(fruit):
#     print(fruit[index])
#     index -= 1

"""
String slices
"""
# s = 'Monty Python'
# print(s[0:5])  # Monty
# print(s[6:12])  # Python
#
# print(s[:5])  # Monty
# print(s[6:])  # Python
# print(s[:])  # Monty Python

"""
String are immutable
"""
# greeting = 'Hello, world!'
# greeting[0] = 'J'  # TypeError: 'str' object does not support item assignment

# greeting = 'J' + greeting[1:]
# print(greeting)

# greeting = f'J{greeting[1:]}'
# print(greeting)

"""
Looping and counting
"""
# Counts the number of times the letter "a" appears in the string "banana"
# count = 0
# for letter in 'banana':
#     if letter == 'a':
#         count += 1
# print(count)


# def count_letter(letter, word):
#     count = 0
#     for char in word:
#         if char == letter:
#             count += 1
#     return count
#
#
# print(count_letter('a', 'banana'))

"""
The in operator
The word in is a boolean operator that takes two strings and returns True if 
the first appears as a substring in the second:
"""
# print('a' in 'banana')  # True
# print('ba' in 'banana')  # True
# print('seed' in 'banana')  # False

"""
String comparison
"""
# word = input('Enter a fruit name: ')

# if word == 'banana':
#     print('All right, bananas.')

# if word < 'banana':
#     print(f'Your word, {word}, comes before banana.')
# elif word > 'banana':
#     print(f'Your word, {word}, comes after banana.')
# else:
#     print('All right, bananas.')


# def compare_string(s1, s2):
#     s1 = s1.lower()
#     s2 = s2.lower()
#     if s1 < s2:
#         print(f'{s1}, comes before {s2}')
#     elif s1 > s2:
#         print(f'{s1}, comes after {s2}')
#     else:
#         print(f'All right, {s1}s')
#
# compare_string('aanana', 'BANANA')
# compare_string('danana', 'BANANA')
# compare_string('banana', 'BANANA')

"""
String methods
"""
# stuff = 'Hello world'
# print(type(stuff))  # <class 'str'>
# print(dir(stuff))  # lists the methods available for an object

# print('banana'.upper())

# print('banana'.find('a'))  # 1
# print('banana'.find('na'))  # 2
# print('banana'.find('na', 3))  # 4
# print('banana'.find('z'))  # -1

#  Remove white space (spaces, tabs, or newlines)
# line = '    Here we go        '
# print(f'{line}Hello')
# print(f'{line.strip()}Hello')

# line = 'Have a nice day'
# print(line.startswith('Have'))  # True
# print(line.startswith('h'))  # False
# print(line.lower().startswith('h'))  # True

# line = 'Have a nice day'
# print(line.count('a'))  # 3
# print(line.count('a', 5))  # 2
# print(line.count('a', 5, 8))  # 1

# print('banana'.count('a'))  # 3

"""
Parse strings
"""
line = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
# line = 'From stephen.marquarduct.ac.za Sat Jan 5 09:14:16 2008'
# line = 'From stephen.marquard@ Sat Jan 5 09:14:16 2008'


# def find_address(string):
#     host = ''
#     space_pos = -1
#     at_pos = string.find('@')
#     if at_pos != -1:
#         space_pos = string.find(' ', at_pos)
#     if space_pos != -1:
#         host = string[at_pos + 1:space_pos]
#     return host
#
#
# address = find_address(line)
# print(address) if len(address) > 0 else print('Can not find')

"""
Format operator
"""
camels = 42
print('I have spotted %d camels.' % camels)  # I have spotted 42 camels.

print('In %d years I have spotted %g %s.' % (3, 0.1, 'camels'))  # In 3 years I have spotted 0.1 camels.

data = (3, 0.1, 'camels')
print(f'In {data[0]} years I have spotted {data[1]} {data[2]}.')  # In 3 years I have spotted 0.1 camels.

























































