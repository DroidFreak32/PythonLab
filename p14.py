# p14.py
'''
Write a function that returns the number of days in a year using the following header:
def numberOfDaysInAYear(year):
Write a test program that displays the number of days in the years from 2010 to 2020.
'''

def numberOfDaysInAYear(year):
    if year%4==0 and year%100!=0 or year%400==0:
        return 366
    else:
        return 365

days=0
yr=2010
while yr<2020:
    days+=numberOfDaysInAYear(yr)
    yr+=1
print("The number of days between 2010 and 2020 are:",days)

#############################################
