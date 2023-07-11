# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    '''
    n is the length of nestedList and d is the max depth and l is the total number of lists within the nested List
    Time: O(n * L)
    Space: O(n * d)
    '''

    def __init__(self, nestedList: List[NestedInteger]):
        self.ind = 0
        self.flat = []

        def dfs(lst):
            for ele in lst:
                if ele.isInteger():
                    self.flat.append(ele.getInteger())
                else:
                    dfs(ele.getList())
        dfs(nestedList)

    '''
    Time: O(1)
    Space: O(1)
    '''

    def next(self) -> int:
        tmp = self.ind
        self.ind += 1
        return self.flat[tmp]

    '''
    Time: O(1)
    Space: O(1)
    '''

    def hasNext(self) -> bool:
        return self.ind < len(self.flat)


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
