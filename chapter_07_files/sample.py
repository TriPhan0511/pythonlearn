"""
Opening files
"""
# try:
#     file_handle = open('mbox-short.txt')
#     print(file_handle)
# except FileNotFoundError:
#     print('Can not find this file!')

"""
Reading files
"""
# count = 0
# try:
#     file_handle = open('mbox-short.txt')
#     for line in file_handle:
#         count += 1
# except FileNotFoundError:
#     print('Cannot open this file!')
# print(f'Line Count: {count}')

"""
Using the read method

If you know the file is relatively small compared to the size of your main memory,
you can read the whole file into one string using the read method on the file handle.

Remember that this form of the open function should only be used if the file data
will fit comfortably in the main memory of your computer. If the file is too large
to fit in main memory, you should write your program to read the file in chunks
using a for or while loop.
"""
# file_handle = open('mbox-short.txt')
# inp = file_handle.read()
# print(len(inp))  # 94626
# print(inp[:20])  # From stephen.marquar

"""
When the file is read in this manner, all the characters including all of the lines
and newline characters are one big string in the variable inp. It is a good idea
to store the output of read as a variable because each call to read exhausts the
resource:
"""
# file_handle = open('mbox-short.txt')
# print(len(file_handle.read()))  # 94626
# print(len(file_handle.read()))  # 0

"""
Searching through a file
"""

# Read a file and only print out lines which started with the prefix "From:"


# def print_lines(file):
#     try:
#         file_handle = open(file)
#         for line in file_handle:
#             if line.startswith('From:'):
#                 print(line.rstrip())
#     except FileNotFoundError:
#         print('Can not find this file!')


"""
As your file processing programs get more complicated, you may want to structure
your search loops using continue. The basic idea of the search loop is that you are
looking for “interesting” lines and effectively skipping “uninteresting” lines. And
then when we find an interesting line, we do something with that line.
"""


# def print_lines(file):
#     try:
#         file_handle = open(file)
#         for line in file_handle:
#             # Skip 'uninteresting' lines
#             if not line.startswith('From:'):
#                 continue
#             # Process our 'interesting' lines
#             print(line.rstrip())
#     except FileNotFoundError:
#         print(f'Can not find file {file}')
#
#
# print_lines('mbox-short.txt')


# Show lines which contain a specified string
# def search(string, file):
#     try:
#         file_handle = open(file)
#         for line in file_handle:
#             if line.find(string) == -1:
#                 continue
#             print(line.rstrip())
#     except FileNotFoundError:
#         print(f'Can not find file {file}')
#
#
# search('@uct.ac.za', 'mbox-short.txt')

# Letting the user choose the file name
# def count_lines(word):
#     file = input('Enter the file name: ')
#     try:
#         file_handle = open(file)
#         count = 0
#         for line in file_handle:
#             if not line.startswith(word):
#                 continue
#             count += 1
#         if count == 0:
#             print('There was not any subject line')
#         elif count == 1:
#             print(f'There was only one subject line in {file}')
#         else:
#             print(f'There were {count} subject lines in {file}')
#     except FileNotFoundError:
#         print(f"No such file or directory: '{file}'.")

# def count_lines(word):
#     file = input('Enter the file name: ')
#     try:
#         file_handle = open(file)
#         count = 0
#         word = word.lower()
#         for line in file_handle:
#             if not line.lower().startswith(word):
#                 continue
#             count += 1
#         if count == 0:
#             print('There was not any subject line')
#         elif count == 1:
#             print(f'There was only one subject line in {file}')
#         else:
#             print(f'There were {count} subject lines in {file}')
#     except FileNotFoundError:
#         print(f"No such file or directory: '{file}'.")

# Using exit() function
# def count_lines(word):
#     file_name = input('Enter the file name: ')
#     try:
#         file_handle = open(file_name)
#     except FileNotFoundError:
#         print(f"No such file or directory: '{file_name}'")
#         exit()
#     count = 0
#     for line in file_handle:
#         if not line.startswith(word):
#             continue
#         count += 1
#     if count == 0:
#         print('There was not any subject line')
#     elif count == 1:
#         print(f'There was only one subject line in {file_name}')
#     else:
#         print(f'There were {count} subject lines in {file_name}')
#
#
# count_lines('Subject')

# ---------------------------------------------------------------------------
"""
Writing files
To write a file, you have to open it with mode "w" as a second parameter
"""
# file_out = open('output.txt', 'w')
# # print(file_out)
# line1 = "This here's the wattle\n"
# file_out.write(line1)
# file_out.close()

# sentences = ['Hello World2', 'How are you?', 'Welcome to Danang']
# file_out = open('output.txt', 'w')
# for sentence in sentences:
#     file_out.write(f'{sentence}\n')
# file_out.close()

# def write_file():
#     file_name = input('Enter a file name: ')
#     print('Type "done" to complete entering text')
#     file_output = open(file_name, 'w')
#     line_index = 1
#     while True:
#         line = input(f'line {line_index}: ')
#         if len(line) > 0 and line.startswith('#'):
#             continue
#         if line == 'done':
#             break
#         file_output.write(f'{line}\n')
#         line_index += 1
#     file_output.close()
#     print('Done!')
#
#
# write_file()


"""
Appending files
"""
# file_out = open('output.txt', 'a')
# file_out.write('Another line')
# file_out.close()

line = '1 2\t3\n4'
print(line)
print(repr(line))






















































