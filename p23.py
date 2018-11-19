# p23.py
'''
Write a program that calculates the future value of an investment at a given interest rate for a specified number of years. The formula for the calculation is as follows:
futureValue = investmentAmount * (1 + monthlyInterestRate) ^ (years * 12)
Use text fields for users to enter the investment amount, years, and interest rate. Display the future amount in a label field when the user clicks the Calculate button, as shown.
'''
from tkinter import *


def processButton():
    futureValue = float(investmt_amt.get()) * pow(1 + (float(annual_intrst_rate.get()/100) / 12), float(years.get()) * 12)
    l5["text"] = str(futureValue)


window = Tk()
window.title("Investment Calculator")
investmt_amt = DoubleVar()
l1 = Label(window, text="Investment Amount")
t1 = Entry(window, textvariable=investmt_amt)
years = DoubleVar()
l2 = Label(window, text="Years")
t2 = Entry(window, textvariable=years)
annual_intrst_rate = DoubleVar()
l3 = Label(window, text="Annual Interest Rate (%)")
t3 = Entry(window, textvariable=annual_intrst_rate)

l4 = Label(window, text="Future Value")
l5 = Label(window)
button = Button(window, text="Calculate", command=processButton)
l1.grid(row="1", column="1")
t1.grid(row="1", column="2")
l2.grid(row="2", column="1")
t2.grid(row="2", column="2")
l3.grid(row="3", column="1")
t3.grid(row="3", column="2")
l4.grid(row="4", column="1")
l5.grid(row="4", column="2")
button.grid(row="5", column="2")
window.mainloop()

#############################################
