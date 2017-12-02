class Quadrangle:
    def __init__(self, point, height, width):
        self._point = point
        self._height = height
        self._width = width

    def getPoint(self):
        return self._point

    def getHeight(self):
        return self._height

    def getWidth(self):
        return self._width

    def setHeight(self, height):
        self._height = height

    def setWidth(self, width):
        self._width = width

    def getPerimetr(self):
        raise NotImplementedError("You forgot to implement method getPerimetr")

    def getArea(self):
        raise NotImplementedError("You forgot to implement method getArea")
        
