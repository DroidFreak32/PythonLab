# p07.py
#Write a program to count the number of each vowel in a given string.

vowels={"a","A","e","E","i","I","o","O","u","U"}
s=input("Enter the string:")
cnt=0
for ch in s:
    if ch in vowels:
        cnt+=1
print("The number of vowels:",cnt)

#############################################
