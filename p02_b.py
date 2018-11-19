# p02_b.py
"""
In the retail application, display the details of the customer like bill id, customer id, bill amount and customer name. But the retail shop wants the customer name to be between 3 to 20 characters. Write a Python Program to implement the case study.
""" 
bill_id = input("Enter the Bill ID : ")
cust_id = input("Enter the Customer ID : ")
bill_amt = float(input("Enter the bill amount : "))
cust_name = input("Enter the Customer name :")
flag = True
while flag:     
    if(len(cust_name)<3 or len(cust_name)>20):
        print("The name is invalid!")
        cust_name=input("Enter the Customer Name : ")     
else:
    flag = False  print("BILL ID : ",bill_id) 
print("CUSTOMER ID : ",cust_id) print("BILL AMOUNT : ",bill_amt) 
print("CUSTOMER NAME : ",cust_name) 

#############################################
