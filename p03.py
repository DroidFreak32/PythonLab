# p03.py
#Write a Python program to check whether the given string is palindrome or not.

def easy_pal(string):
    if string == string[::-1]:
        print(string + " is a palindrome")
    else:
        print(string + " is not a palindrome")

def harder_pal(string):
    LENGTH = len(string)

    for i in range(LENGTH//2):
        if string[i] != string[LENGTH - i - 1]:
            print(string + " is not a palindrome")
            return

    print(string + " is a palindrome")

inp = input("Enter a string: ")

easy_pal(inp)

harder_pal(inp)

#############################################
