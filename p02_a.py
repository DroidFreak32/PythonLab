# p02_a.py
"""
The finance department of a company wants to calculate the monthly net pay of one of its employee by finding the income tax to be paid (in Indian Rupees) and the net salary after the income tax deduction. The employee should pay the income tax based on the following table:
Gross Salary(In Rs) | Tax Percentage
--------------------|---------------
Below 5,000         | Nil
5,001 to 10,000     | 10%
10,001 to 20,000    | 20%
More than 20,000    | 30%

Display the employee id, basic salary, allowances, gross pay, income tax and net pay using Python Programming.
"""

emp_id = int(input("Enter Employee ID : "))
basic_pay = float(input("Enter Basic Pay : "))
allowances = float(input("Enter Allowances : "))

gross_pay = basic_pay + allowances

if gross_pay > 20000:
    income_tax = gross_pay * 0.3
elif gross_pay > 10000:
    income_tax = gross_pay * 0.2
elif gross_pay > 5000:
    income_tax = gross_pay * 0.1
else:
    income_tax = 0

net_pay = gross_pay - income_tax

print("Employee ID : ", emp_id)
print("Basic Pay   : Rs", basic_pay)
print("Allowances  : Rs", allowances)
print("Gross Pay   : Rs", gross_pay)
print("Income Tax  : Rs", income_tax)
print("Net Pay     : Rs", net_pay)

#############################################
