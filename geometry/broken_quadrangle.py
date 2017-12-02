from geometry.quadrangle import Quadrangle

class BrokenQuadrangle(Quadrangle):
    def __init__(self, point, height, width):
        super(BrokenQuadrangle, self).__init__(point, height, width)

# Methods getPerimetr() and getArea() are intentionally not implemented
