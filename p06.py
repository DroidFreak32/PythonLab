# p06.py
#Write a program to count and display the number of capital letters in a given string.

s=input("Enter the string")
cnt=0
for ch in s:
    if ch.isupper():
        cnt+=1
print("The number of capital letters are:",cnt)

#############################################
