from random import randint
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def printInterval(self):
        print('('+str(self.start)+","+str(self.end)+")")

    @staticmethod
    def generateRandomIntervalPairWithInRange(start, end):
        left = randint(start, end)
        right = randint(start, end)
        if(left>right):
            left, right = right, left
        return Interval(left, right)