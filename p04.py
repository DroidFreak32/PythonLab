# p04.py
#Write a Python program to generate first ‘n’ Fibonacci numbers.

def fibonaci(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fibonaci(n-1)+fibonaci(n-2)

n=int(input("Enter n:"))
print("The fibonacci series:")
for i in range(n):
    print(fibonaci(i))

#############################################
