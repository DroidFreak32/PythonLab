# p21.py
'''
Design a class named Triangle that extends the GeometricObject class. The Triangle class contains:
* Three float data fields named side1 , side2 , and side3 to denote the three sides of the triangle.
* A constructor that creates a triangle with the specified side1 , side2 , and side3 with default values 1.0 .
* The accessor methods for all three data fields.
* A method named getArea() that returns the area of this triangle.
* A method named getPerimeter() that returns the perimeter of this triangle.
* A method named __str__() that returns a string description for the triangle.
Write a test program that prompts the user to enter the three sides of the triangle, a color, and 1 or 0 to indicate whether the triangle is filled. The program should create a Triangle object with these sides and set the color and filled properties using the input. The program should display the triangle’s area, perimeter, color, and True or False to indicate whether the triangle is filled or not.
'''

import math

class GeometricObject:
    def __init__(self, color, filled):
        self.color = color
        self.filled = filled

    def getPerimeter(self):
        pass
    def getArea(self):
        pass
    def getColor(self):
        return self.color
    def getFilled(self):
        return self.filled

class Triangle(GeometricObject):
    '''
    Represents a triangle having sides s1,,s2 and s3.Computes Areas and also the Perimeter
    '''
    def __init__(self, color, filled, side1 = 1.0, side2 = 1.0, side3 = 1.0):
        GeometricObject.__init__(self, color, filled)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    # Accessor methods
    def getSide1(self):
        return self.side1
    def getSide2(self):
        return self.side2
    def getSide3(self):
        return self.side3
    def getPerimeter(self):
        return self.side1 + self.side2 + self.side3
    def getArea(self):
        # Heron's formula
        p = self.getPerimeter() / 2;
        area = math.sqrt(p * (p - self.side1) * (p - self.side2) * (p - self.side3))
        return area

    def __str__(self):
        return Triangle.__doc__ #returns the comment inder the class
    # def __str__(self):
    #     return  "Side 1    : " + str(self.side1) + "\n" + \
    #             "Side 2    : " + str(self.side2) + "\n" + \
    #             "Side 3    : " + str(self.side3) + "\n" + \
    #             "Perimeter : " + str(self.getPerimeter()) + "\n" + \
    #             "Area      : " + str(self.getArea()) + "\n" + \
    #             "Filled    : " + str(self.filled) + "\n" + \
    #             "Color     : " + str(self.color)

triangle1 = Triangle("RED", True)
print(triangle1)

#############################################
