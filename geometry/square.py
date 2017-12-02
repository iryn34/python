from geometry.rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, point, side):
        super(Square, self).__init__(point, side, side)

    def getPoint(self):
        return self._point

    def getSide(self):
        return self.getHeight()

    def setSide(self, side):
        self.setHeight(side)

    def getPerimetr(self):
        return 4 * self.getSide()

    def getArea(self):
        return self.getSide() * self.getSide()
