# p08.py
#Write a program to remove all punctuations like “’!()-[]{};:’’’,\,<>,/,?,@,#,$, %^&*_~” from the string provided by the user.

s=input("Enter the string:")
for ch in s:
    if ch in "'!()-[];:,\\<>/?@#$%^&*_~\"": #To include " give it as /"
        s=s.replace(ch,"")
print(s)

#############################################
