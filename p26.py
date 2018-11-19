# p26.py
#MultiThreading - one thread to print number of vowels and other to check palindrome

from threading import Thread
import time

class Mythread(Thread):
    def __init__(self,threadID,name,string):
        Thread.__init__(self)
        self.name=name
        self.string=string
        self.threadID=threadID
    def run(self):
        print("Starting ",self.name)
        if self.threadID==1:
            self.vowelcount()
        else:
            self.palindrome()
        print("Exiting ",self.name)
    def vowelcount(self):
        vowels={"a","A","e","E","i","I","o","O","u","U"}
        cnt=0
        for ch in self.string:
            if ch in vowels:
                cnt+=1
        print("The number of vowels:",cnt)  
    def palindrome(self):
        srev=self.string[::-1]
        if self.string==srev:
            print("String is a palindrome")
        else:
            print("String is not a palindrome")
            
            
thread1=Mythread(1,"Find Vowel","I love Python Programming")
thread2=Mythread(2,"Palindrome","malayalam")
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("Exiting main thread")

#############################################
