# p05.py
"""
Consider the scenario of processing marks of students for a course in student management system. Given below is the list of marks scored by students. Find top three scorers for the course and also display the average marks scored by all students. Implement the solution using Python Programming. Student Name Marks Scored
John    |86.5
Jack    |91.2
Jill    |84.5
Harry   |72.1
Joe     |80.5
"""

student={"John":86.5,"Jack":91.2,"Jill":84.5,"Harry":72.1,"Joe":80.5}
marks=list(student.values())
marks.sort()#The top three scorers will be the last three marks holders
for s in student:#To get the name for the top scorer marks
    if student[s]==marks[len(marks)-1]:
        top1=s
    elif student[s]==marks[len(marks)-2]:
        top2=s
    elif student[s]==marks[len(marks)-3]:
        top3=s
#To compute the average
avg=0
for i in marks:
    avg+=i 
avg/=len(marks)

print("The top three scorers are:",top1,",",top2,",",top3)
print("The average score:",avg)

#############################################
