class Circle:
    def __init__(self, point, radius):
        self._point = point
        self._radius = radius

    def getPoint(self):
        return self._point

    def getRadius(self):
        return self._radius

    def isWider(self, anotherCircle):
        return self.getRadius() > anotherCircle.getRadius()

    def isHigher(self, anotherCircle):
        return self.isWider(anotherCircle)
