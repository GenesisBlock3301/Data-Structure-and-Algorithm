class Difference:
    maximumDifference = 0
    def __init__(self, a):
        self.__elements = a

    def computeDifference(self):
        minVal = min(self.__elements)
        maxVal = max(self.__elements)
        self.maximumDifference = maxVal - minVal


# Add your code here

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
