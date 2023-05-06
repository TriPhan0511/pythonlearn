"""
The while loop
"""
# n = 5
# while n > 0:
#     print(n)
#     n -= 1
# print('Blastoff!')

"""
The break keyword
"""
# while True:
#     line = input('>')
#     if line == 'done':
#         break
#     print(line)
# print('Done!')

"""
The continue keyword
"""
# while True:
#     line = input('>')
#     if line == '#':
#         continue
#     if line == 'done':
#         break
#     print(line)
# print('Done!')

"""
The for loop
"""
# friends = ['Alex', 'Mary', 'Peter']
# for friend in friends:
#     print(f'Aloha {friend}')
# print('Done')

"""
Loop patterns
"""

"""
Counting and summing loops
"""
# count = 0
# for num in [1, 3, 2, 6, 8]:
#     count += 1
# print(f'Count: {count}')

# total = 0
# for num in [1, 2, 3, 4, 5]:
#     total += num
# print(f'Total: {total}')


"""
Maximum and minimum loop
"""
# largest = None
# for num in [4, 3, 5, 6, 9, 3]:
#     if largest is None or num > largest:
#         largest = num
# print(f'Maximum value: {largest}')


# smallest = None
# for num in [4, 3, 5, 6, 9, 3]:
#     if smallest is None or num < smallest:
#         smallest = num
# print(f'Minimum value: {smallest}')

# print(min([4, 3, 5, 6, 9, 3]))

def findMin(values):
    smallest = None
    for value in values:
        if smallest is None or value < smallest:
            smallest = value
    return smallest


print(findMin([4, 3, 5, 6, 9, 3]))











































