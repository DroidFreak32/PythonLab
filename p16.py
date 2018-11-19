# p16.py
#To grade MCQ of students based on the answer key

student=[["A","B","A","C","C","D","E","E","A","D"],
         ["D","B","A","B","A","D","E","E","A","D"],
         ["E","D","D","A","B","D","E","E","A","D"],
         ["C","B","A","E","D","C","E","E","A","D"],
         ["A","B","D","C","C","D","E","E","A","D"],
         ["B","B","E","C","C","D","E","E","A","D"],
         ["B","B","A","C","C","D","E","E","A","D"],
         ["E","B","E","C","C","D","E","E","A","D"]]

answer=["D","B","D","C","C","D","A","E","A","D"]
cnt=0 # For student number
for s in student: #s refers to individual student
    marks=0
    i=0
    while i<len(answer): # Compare every key and the answer
        if s[i]==answer[i]:
            marks+=1
        i+=1
    print("The marks of student ",cnt,":",marks)
    cnt+=1
    
#############################################
