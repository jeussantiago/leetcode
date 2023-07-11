from sortedcontainers import SortedSet


class SummaryRanges:
    '''
    when we add a number, we can see if it fits in one of the ranges

    addNum:
        Time: O(logn) logn for binary tree insrt
        Space: O(n)

    getIntervals:
        Time: O(n)
        Space: O(n) extra space for the result

    '''

    def __init__(self):
        self.interval = SortedSet()

    def addNum(self, value: int) -> None:
        self.interval.add(value)

    def getIntervals(self) -> List[List[int]]:
        res = []
        lowerRange = 0
        while lowerRange < len(self.interval):
            tmp = lowerRange
            upperRange = self.interval[lowerRange]
            while upperRange + 1 in self.interval:
                upperRange += 1
                tmp += 1
            res.append([self.interval[lowerRange], upperRange])
            lowerRange = tmp + 1

        return res


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()
