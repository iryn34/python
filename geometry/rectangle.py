from geometry.quadrangle import Quadrangle

class Rectangle(Quadrangle):
    def __init__(self, point, height, width):
        super(Rectangle, self).__init__(point, height, width)

    def getPerimetr(self):
        return 2 * self.getHeight() + 2 * self.getWidth()

    def getArea(self):
        return self.getHeight() * self.getWidth()

    def isWider(self, anotherRectangle):
        return self.getWidth() > anotherRectangle.getWidth()

    def isHigher(self, anotherRectangle):
        return self.getHeight() > anotherRectangle.getHeight()
