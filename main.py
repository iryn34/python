from geometry.point import Point
from geometry.quadrangle import Quadrangle
from geometry.broken_quadrangle import BrokenQuadrangle
from geometry.rectangle import Rectangle
from geometry.square import Square
from geometry.quadrangles_collection import QuadranglesCollection
from geometry.circles_collection import CirclesCollection
from geometry.circle import Circle
# import point as p
#
# point = Point(2, 3)
# point.printPoint()
#
# listOfQuadrangles = []
#
# listOfQuadrangles.append(Rectangle(point, 4, 3))   #14
# listOfQuadrangles.append(Rectangle(point, 4, 5))   #18
# listOfQuadrangles.append(Rectangle(point, 1, 3))   #8
# listOfQuadrangles.append(Rectangle(point, 2, 3))   #10
# listOfQuadrangles.append(Rectangle(point, 4, 5))   #18
#
# listOfQuadrangles.append(BrokenQuadrangle(point, 2, 1))
# listOfQuadrangles.append(BrokenQuadrangle(point, 1, 2))
# listOfQuadrangles.append(BrokenQuadrangle(point, 4, 1))
#
# listOfQuadrangles.append(Square(point, 3))   #12
#
# x = float(input("Enter x: "))
# y = float(input("Enter y: "))
# height = float(input("Enter height: "))
# width = float(input("Enter width: "))
# point = Point(x, y)
# listOfQuadrangles.append(Rectangle(point, height, width))  #10
#
# # square = Square(point, 3)
# # print (square.getArea())
#
# print (listOfQuadrangles)
#
# sum = 0
# for quadrangle in listOfQuadrangles:
#     try:
#         sum += quadrangle.getPerimetr()
#     except NotImplementedError:
#         print ("Broken Quadrangle")

# print (sum)

# quadranglesCollection = QuadranglesCollection([
#     Rectangle(Point(0, 0), 6, 3),
#     Rectangle(Point(1, 1), 3, 4),
#     Rectangle(Point(2, 2), 4, 5)
# ])
#
# print (quadranglesCollection.getTheWidest().getPoint().getX())
# print (quadranglesCollection.getTheHighest().getPoint().getX())

circlesCollection = CirclesCollection([
    Circle(Point(0, 0), 6),
    Circle(Point(1, 1), 3),
    Circle(Point(2, 2), 4)
])

print (circlesCollection.getTheWidest().getPoint().getX())
print (circlesCollection.getTheHighest().getPoint().getX())
