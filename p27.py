# p27.py
'''Design a Tkinter interface to perform the following operations on a database by considering the table
Student (USN: String, Name: String, Age: Int, Branch: String).
Display the success and failure message using MessageBox
a. Insert student details 
b. Search the student details with USN=”4NM06CS001"'''
import pymysql
from tkinter import *
from tkinter import messagebox

mydb=pymysql.connect(host="localhost",user="root",passwd="root",database="stud")
mycursor=mydb.cursor()

def processInsert():
    sql="INSERT INTO Student VALUES ('"+var1.get()+"','"+var2.get()+"','"+str(var3.get())+"','"+var4.get()+"')"
    try:
        mycursor.execute(sql)
        mydb.commit()
        messagebox.showinfo("Insertion","Insertion successful")
    except:
        messagebox.showerror("Insertion","Insertion Unsuccessful")
        mydb.rollback()
    
def processSearch():
    sql="SELECT * FROM Student WHERE USN='"+var1.get()+"'"
    mycursor.execute(sql)
    for row in mycursor:
        if(var1.get()==row[0]):
            messagebox.showinfo("Search","Search successful")
            var1.set(row[0])
            var2.set(row[1])
            var3.set(row[2])
            var4.set(row[3])
            return
    messagebox.showerror("Search","Search Unsuccessful")
    
window=Tk()
window.title("Student")
l1=Label(window,text="USN")
l2=Label(window,text="Name")
l3=Label(window,text="Age")
l4=Label(window,text="Branch")
var1=StringVar()
var2=StringVar()
var3=IntVar()
var4=StringVar()
t1=Entry(window,textvariable=var1)
t2=Entry(window,textvariable=var2)
t3=Entry(window,textvariable=var3)
t4=Entry(window,textvariable=var4)
b1=Button(window,text="Insert",command=processInsert)
b2=Button(window,text="Search",command=processSearch)
l1.grid(row="1",column="1")
t1.grid(row="1",column="2")
l2.grid(row="2",column="1")
t2.grid(row="2",column="2")
l3.grid(row="3",column="1")
t3.grid(row="3",column="2")
l4.grid(row="4",column="1")
t4.grid(row="4",column="2")
b1.grid(row="5",column="1")
b2.grid(row="5",column="2")
window.mainloop()

#############################################
