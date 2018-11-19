# p12.py
'''
Design a class named Rectangle to represent a rectangle. class contains:
* Two data fields named width and height .
* A constructor that creates a rectangle with the specified width and height .
* The default values are 1 and 2 for the width and height, respectively.
* A method named getArea() that returns the area of this rectangle.
* A method named getPerimeter() that returns the perimeter.
Write a test program that creates two Rectangle objects—one with width 4 and height 40 and the other with width 3.5 and height 35.7. Display the width, height, area, and perimeter of each rectangle in this order.
'''

class Rectangle:
    def __init__(self,width=1,height=2):
        self.width=width
        self.height=height
    def getArea(self):
        return self.width*self.height
    def getPerimeter(self):
        return 2*(self.width+self.height)

def main():
    r1=Rectangle(4,40)
    r2=Rectangle(3.5,35.7)
    print("For Rectangle 1:")
    print("Width:",r1.width," Height:",r1.height," Area:",r1.getArea()," Perimeter:",r1.getPerimeter())
    print("For Rectangle 2:")
    print("Width:",r2.width," Height:",r2.height," Area:",r2.getArea()," Perimeter:",r2.getPerimeter())
    
main()

#############################################
