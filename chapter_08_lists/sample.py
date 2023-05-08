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
# cars = [
#     {'car': 'Ford', 'year': 2005},
#     {'car': 'Mitsubishi', 'year': 2000},
#     {'car': 'BMW', 'year': 2019},
#     {'car': 'VW', 'year': 2011},
#     {'car': 'ABCDEF'},
# ]
#
#
# def get_year(e):
#     return e['year']
#
#
# cars.sort(key=get_year)
# print(cars)
# # [
# #     {'car': 'Mitsubishi', 'year': 2000},
# #     {'car': 'Ford', 'year': 2005},
# #     {'car': 'VW', 'year': 2011},
# #     {'car': 'BMW', 'year': 2019}
# # ]

"""Deleting elements"""

"""
If you know the index of the element you want, you can use pop
If you don't provide an index, it deletes and returns the last element.
"""
# t = ['a', 'b', 'c']

# x = t.pop(1)
# print(t)  # ['a', 'c']
# print(x)  # b

# y = t.pop()
# print(t)  # ['a', 'b']
# print(y)  # c

"""
If you know the element you want to remove (but not the index), you can use remove.
The return value from remove is None.
"""
# t = ['a', 'b', 'c']

# t.remove('b')
# print(t)  # ['a', 'c']

# t.remove('d')  # ValueError: list.remove(x): x not in list

# if 'd' in t:
#     t.remove('d')

"""To remove more than one element, you can use del with a slice index"""
# t = ['a', 'b', 'c', 'd', 'e', 'f']
# del t[2:5]
# print(t)  # ['a', 'b', 'f']

"""
There are a number of built-in functions that can be used on lists that allow you
to quickly look through a list without writing your own loop

The sum() function only works when the list elements are numbers. The other
functions (max(), len(), etc.) work with lists of strings and other types that can
be comparable.
"""

# nums = [3, 41, 12, 9, 74, 15]
# print(len(nums))  # 6
# print(max(nums))  # 74
# print(min(nums))  # 3
# print(sum(nums))  # 154
# print(sum(nums) / len(nums))  # 25.666666666666668
# print(round(sum(nums) / len(nums), 2))  # 25.67


# def compute_average():
#     total = 0
#     count = 0
#     print('Type "done" if you want to finish entering number')
#     while True:
#         inp = input('Enter a number: ')
#         if inp == 'done':
#             break
#         try:
#             inp = float(inp)
#         except ValueError:
#             print('Incorrect format. Please enter a number!')
#             continue
#         total += inp
#         count += 1
#     if count != 0:
#         return total / count
#     return None

def compute_average():
    print('Type "done" if you want to finish entering number')
    t = []
    while True:
        inp = input('Enter a number: ')
        if inp == 'done':
            break
        try:
            inp = float(inp)
        except ValueError:
            print('Wrong format. Please enter a number!')
            continue
        t.append(inp)
    if len(t) == 0:
        return None
    return sum(t)/len(t)


result = compute_average()
if result is None:
    print('Can not compute average')
else:
    print(result)


















































