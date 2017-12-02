from geometry.comparable import Comparable

class CirclesCollection(Comparable):
    def __init__(self, listOfCircles):
        self._listOfCircles = listOfCircles

    def getListOfCircles(self):
        return self._listOfCircles

    def getTheWidest(self):
        theWidest = self.getListOfCircles()[0]

        for index in range(1, len(self.getListOfCircles())):
            if self.getListOfCircles()[index].isWider(theWidest):
                theWidest = self.getListOfCircles()[index]

        return theWidest

    def getTheHighest(self):
        theHighest = self.getListOfCircles()[0]

        for index in range(1, len(self.getListOfCircles())):
            if self.getListOfCircles()[index].isHigher(theHighest):
                theHighest = self.getListOfCircles()[index]

        return theHighest
