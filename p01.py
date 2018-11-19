# p01.py
"""
The finance department of a company wants to calculate the monthly pay of one of its employee. Monthly pay should be calculated as mentioned in the formula below and display all the employee details. Monthly Pay= No. of hours worked in a week * Pay rate per hour * No .of weeks in a month Write a Python Program to implement the problem.
"""

week_hours = float(input("Enter weekly working hours : "))
hourly_pay = float(input("Enter pay rate per hour : "))
working_weeks = float(input("Enter working weeks in a month : "))

monthly_pay = week_hours * hourly_pay * working_weeks

print("Calculated monthly pay : Rs", monthly_pay)

#############################################
