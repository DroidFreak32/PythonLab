# p25.py
# Custom exception TriangleError
import math
import sys
class TriangleError(RuntimeError):
    def __init__(self,s1,s2,s3):
        self.__side1=s1
        self.__side2=s2
        self.__side3=s3
    def getS1(self):
        return self.__side1
    def getS2(self):
        return self.__side2
    def getS3(self):
        return self.__side3
    def printError(self):
        print("The sum of any two sides of a triangle must always be greater than the third side")
        sys.exit()

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
Represents a triangle having sides s1,s2 and s3.Computes Areas and also the Perimeter
    '''
    def __init__(self, color, filled, side1 = 1.0, side2 = 1.0, side3 = 1.0):
        GeometricObject.__init__(self, color, filled)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        try:
            if self.side1+self.side2<=self.side3 or self.side1+self.side3<=self.side2 or self.side3+self.side2<=self.side1:
                raise TriangleError(self.side1,self.side2,self.side3)
            else:
                pass
        except TriangleError as e:
            e.printError()

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

triangle1 = Triangle("RED", True, 5,8,4)
print(triangle1)
triangle2 = Triangle("RED", True, 2,2,8)

#############################################
