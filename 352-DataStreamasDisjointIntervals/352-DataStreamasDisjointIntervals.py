class SummaryRanges:

    def __init__(self):
        self.included = [False] * 10001
        self.startIndexed = {}
        self.endIndexed = {}

    def addNum(self, value: int) -> None:
        if self.included[value]:
            return
        self.included[value] = True
        if value - 1 not in self.endIndexed and value + 1 not in self.startIndexed:
            self.endIndexed[value] = value
            self.startIndexed[value] = value
            return
        if value - 1 in self.endIndexed and value + 1 in self.startIndexed:
            newStart = self.endIndexed[value - 1]
            newEnd = self.startIndexed[value + 1]
            del self.endIndexed[newEnd]
            del self.endIndexed[value - 1]
            del self.startIndexed[newStart]
            del self.startIndexed[value + 1]
            self.startIndexed[newStart] = newEnd
            self.endIndexed[newEnd] = newStart
        elif value - 1 in self.endIndexed:
            newEnd = value
            start = self.endIndexed[value - 1]
            del self.endIndexed[value - 1]
            self.endIndexed[value] = start
            self.startIndexed[start] = value
        elif value + 1 in self.startIndexed:
            newStart = value
            end = self.startIndexed[value + 1]
            del self.startIndexed[value + 1]
            self.startIndexed[value] = end
            self.endIndexed[end] = value

    def getIntervals(self) -> List[List[int]]:
        print(self.startIndexed)
        res = []
        for k in self.startIndexed.keys():
            print(k)
            res.append([k, self.startIndexed[k]])
        res.sort()
        return res


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()