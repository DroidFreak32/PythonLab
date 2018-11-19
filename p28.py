# p28.py
'''Design a Tkinter interface to perform the following operations on a database by considering the table 
Employee (SSN:Int, Fname: String, LName: String, Age: Int,Place: String, Salary: Int).
Display the success and failure message using MessageBox
a. Insert employee details
b. Delete the details of employee whose id = 1001 and place = “XYZ”
c. Update the employee details'''
import pymysql
from tkinter import *
from tkinter import messagebox
mydb=pymysql.connect(host="localhost",user="root",passwd="root",database="Emp")
mycursor=mydb.cursor()

def processInsert():
    sql="INSERT INTO Employee VALUES ('"+var1.get()+"','"+var2.get()+"','"+var3.get()+"','"+str(var4.get())+"','"+var5.get()+"','"+str(var6.get())+"')"
    try:
        mycursor.execute(sql)
        mydb.commit()
        messagebox.showinfo("Insertion","Insertion successful")
    except:
        messagebox.showerror("Insertion","Insertion Unsuccessful")
        mydb.rollback()
    
def processDelete():
    sql="DELETE FROM Employee WHERE SSN='"+var1.get()+"'"
    try:
        mycursor.execute(sql)
        mydb.commit()
        messagebox.showinfo("Deletion","Deletion successful")
    except:
        messagebox.showerror("Deletion","Deletion Unsuccessful")
        mydb.rollback()
        
def processUpdate():
    sql="UPDATE Employee SET Fname='"+var2.get()+"', Lname='"+var3.get()+"', Age='"+str(var4.get())+"', Place='"+var5.get()+"', Salary='"+str(var6.get())+"' WHERE SSN='"+var1.get()+"'"
    try:
        print(sql)
        mycursor.execute(sql)
        mydb.commit()
        messagebox.showinfo("Updation","Updation successful")
    except:
        messagebox.showerror("Updation","Updation Unsuccessful")
        mydb.rollback()
    
window=Tk()
window.title("Employee")
l1=Label(window,text="SSN")
l2=Label(window,text="First Name")
l3=Label(window,text="Last Name")
l4=Label(window,text="Age")
l5=Label(window,text="Place")
l6=Label(window,text="Salary")
var1=StringVar()
var2=StringVar()
var3=StringVar()
var4=IntVar()
var5=StringVar()
var6=IntVar()
t1=Entry(window,textvariable=var1)
t2=Entry(window,textvariable=var2)
t3=Entry(window,textvariable=var3)
t4=Entry(window,textvariable=var4)
t5=Entry(window,textvariable=var5)
t6=Entry(window,textvariable=var6)
b1=Button(window,text="Insert",command=processInsert)
b2=Button(window,text="Delete",command=processDelete)
b3=Button(window,text="Update",command=processUpdate)
l1.grid(row="1",column="1")
t1.grid(row="1",column="2")
l2.grid(row="2",column="1")
t2.grid(row="2",column="2")
l3.grid(row="3",column="1")
t3.grid(row="3",column="2")
l4.grid(row="4",column="1")
t4.grid(row="4",column="2")
l5.grid(row="5",column="1")
t5.grid(row="5",column="2")
l6.grid(row="6",column="1")
t6.grid(row="6",column="2")
b1.grid(row="7",column="1")
b2.grid(row="7",column="2")
b3.grid(row="8",column="1",columnspan="2")
window.mainloop()

#############################################
