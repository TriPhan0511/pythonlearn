# numbers = [10, 20, 30, 40]
# print(numbers)

# numbers[0] = 20000
# print(numbers)

# print(numbers[:2])

# print(numbers[-1])

# print(20 in numbers)

"""
Traversing a list
"""
# cheeses = ['Cheddar', 'Edam', 'Gouda']

# for cheese in cheeses:
#     print(cheese)


# numbers = [1, 2, 3, 4, 5]
# print(numbers)
#
# for i in range(len(numbers)):
#     numbers[i] *= 2
# print(numbers)

# A for loop over an empty list never executes the body:
# empty = []
# for x in empty:
#     print('This never happens')

"""List operations"""

"""The + operator concatenates lists"""
# a = [1, 2, 3]
# b = [4, 5, 6]
# c = a + b
# print(c)  # [1, 2, 3, 4, 5, 6]

"""The * operator repeats a list a given number of times"""
# print([0] * 4)  # [0, 0, 0, 0]
# print([1, 2, 3] * 3)  # [1, 2, 3, 1, 2, 3, 1, 2, 3]

"""List slices"""
# t = ['a', 'b', 'c', 'd', 'e', 'f']
# print(t[1:3])  # ['b', 'c]
# print(t[:4])  # ['a', 'b', 'c', 'd']
# print(t[3:])  # ['d', 'e', 'f']
# print(t[:])  # ['a', 'b', 'c', 'd', 'e', 'f']

# nums1 = [1, 2, 3]
# print(f'Nums1: {nums1}')

# nums2 = nums1
# print(f'Nums2: {nums2}')
#
# nums2[0] = 1000
# print(f'Nums1: {nums1}')
# print(f'Nums2: {nums2}')

# nums3 = nums1[:]
# print(f'Nums3: {nums3}')
#
# nums3[0] = 30000
# print(f'Nums1: {nums1}')
# print(f'Nums3: {nums3}')

"""A slice operator on the left side of an assignment can updated multiple elements"""
# t = ['a', 'b', 'c', 'd', 'e', 'f']
# print(t)

# t[1:3] = ['x', 'y']
# print(t)  # ['a', 'x', 'y', 'd', 'e', 'f']

# t[1:3] = ['r']
# print(t)  # ['a', 'r', 'd', 'e', 'f']

"""List methods"""

"""append adds a new element to the end of a list"""
# t = [1, 2, 3]
# print(t)

# t.append(4)
# print(t)  # [1, 2, 3, 4]

"""extend takes a list as a argument and appends all of the elements"""
# t1 = ['a', 'b', 'c']
# t2 = ['d', 'e']
# t1.extend(t2)
# print(t1)  # ['a', 'b', 'c', 'd', 'e']
# print(t2)  # ['d', 'e']

"""sort arranges the elements of the list from low to high"""
# numbers = [10, 3, 5, 4, 1, 2]
# numbers.sort()
# print(numbers)  # [1, 2, 3, 4, 5, 10]


# characters = ['d', 'c', 'e', 'b', 'a']
# characters.sort()
# print(characters)  # ['a', 'b', 'c', 'd', 'e']

# characters = ['d', 'c', 'e', 'b', 'a']
# characters.sort(reverse=True)
# print(characters)  # ['e', 'd', 'c', 'b', 'a']

# cars = ['Ford', 'BMW', 'Volvo']

# cars.sort()
# print(cars)  # ['BMW', 'Ford', 'Volvo']

# cars.sort(reverse=True)
# print(cars)  # ['Volvo', 'Ford', 'BMW']

"""Sort the list by the length of the values"""
# cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']


# def get_length(e):
#     return len(e)


# cars.sort(key=get_length)
# print(cars)  # ['VW', 'BMW', 'Ford', 'Mitsubishi']

"""Sort the list by the length of the values and reversed"""
# cars.sort(key=get_length, reverse=True)
# print(cars)

"""Sort a list of dictionaries based on the "year" value of the dictionaries"""
# item = {'car': 'Ford', 'year': 2005}
# print(type(item['year']))
cars = [
    {'car': 'Ford', 'year': 2005},
    {'car': 'Mitsubishi', 'year': 2000},
    {'car': 'BMW', 'year': 2019},
    {'car': 'VW', 'year': 2011},
    {'car': 'ABCDEF'},
]


def get_year(e):
    return e['year']


cars.sort(key=get_year)
print(cars)
# [
#     {'car': 'Mitsubishi', 'year': 2000},
#     {'car': 'Ford', 'year': 2005},
#     {'car': 'VW', 'year': 2011},
#     {'car': 'BMW', 'year': 2019}
# ]













