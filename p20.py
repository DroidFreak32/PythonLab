# p20.py
'''
Suppose that a text file contains an unspecified number of scores. Write a program that reads the scores from the file and displays their total and average. Scores are separated by blanks. Your program should prompt the user to enter a filename.
'''

file_name = input("Enter file name : ")

try:
    file = open(file_name)
    scores = []

    total,n = 0,0
    for line in file:
        scores = line.split(' ')
        scores = list(map(int, scores))
        n+=len(scores)
        print(scores)
        for score in scores:
            total += score
    
    print("Total score : ", total)
    print("Average score : ", total / n)

except FileNotFoundError:
    print("file not found")

#############################################
