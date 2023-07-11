# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        '''
        BFS:
        [NestedInteger{_integer: 1, _list: []}, NestedInteger{_integer: 1, _list: []}]
        None
        ------
        []
        2
        ------
        [NestedInteger{_integer: 1, _list: []}, NestedInteger{_integer: 1, _list: []}]
        None
        ------

        n is the len of the nestedList and m is the max depth of the nestedlist
        Time: O(n * m)
        '''

        queue = collections.deque([ele for ele in nestedList])
        total, depth = 0, 1
        while queue:
            for _ in range(len(queue)):
                ele = queue.pop()
                if ele.isInteger():
                    total += ele.getInteger() * depth
                else:
                    for item in ele.getList():
                        queue.appendleft(item)

            depth += 1

        return total


class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        '''
        DFS

        '''

        def dfs(lst, depth):
            total = 0
            for ele in lst:
                if ele.isInteger():
                    total += ele.getInteger() * depth
                else:
                    total += dfs(ele.getList(), depth + 1)
            return total

        return dfs(nestedList, 1)
