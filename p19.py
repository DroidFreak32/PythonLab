# p19.py
'''
Write a program that will count the number of characters, words, and lines in a file. Words are separated by a white-space character. Your program should prompt the user to enter a filename.
'''

file_name = input("Enter file name : ").strip()

try:
    file = open(file_name) # Or use "if not(os.path.isfile(fname)):" import os.path
    word_count = 0
    line_count = 0
    char_count = 0
    for line in file:
        line_count += 1
        char_count += len(line) # len(line.strip()) To ignore the newline chars
        words=line.split(" ")
        word_count += len(words) # OR word_count += line.count(' ') + 1   ## number of spaces + 1

    print("Number of Lines : ", line_count)
    print("Number of Words : ", word_count)
    print("Number of Chars : ", char_count)

except FileNotFoundError:
    print("file not found")

#############################################
