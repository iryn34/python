from geometry.comparable import Comparable

class QuadranglesCollection(Comparable):
    def __init__(self, listOfQuadrangles):
        self._listOfQuadrangles = listOfQuadrangles

    def getListOfQuadrangles(self):
        return self._listOfQuadrangles

    def getTheWidest(self):
        theWidest = self.getListOfQuadrangles()[0]

        for index in range(1, len(self.getListOfQuadrangles())):
            if self.getListOfQuadrangles()[index].isWider(theWidest):
                theWidest = self.getListOfQuadrangles()[index]

        return theWidest

    def getTheHighest(self):
        theHighest = self.getListOfQuadrangles()[0]

        for index in range(1, len(self.getListOfQuadrangles())):
            if self.getListOfQuadrangles()[index].isHigher(theHighest):
                theHighest = self.getListOfQuadrangles()[index]

        return theHighest
