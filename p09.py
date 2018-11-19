# p09.py
'''
Consider two strings, String1 and String2 and display the merged_string as output. The merged_string should be the capital letters from both the strings in the order they appear. Sample Input: String1: I Like C String2: Mary Likes Python Merged_string should be ILCMLP
'''

String1=input("Enter string 1:")
String2=input("Enter string 2:")
merged_string=""
for ch in String1:
    if ch.isupper():
        merged_string=merged_string+ch
for ch in String2:
    if ch.isupper():
        merged_string=merged_string+ch
print(merged_string)

#############################################
