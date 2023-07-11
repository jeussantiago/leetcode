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
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        '''
        w is the biggest amount of NestedInteger is a depth level
        n is the total amount of nestedInteger
        Time: O(n) ; (n) for getting all the values
                   ; (n) for calculating the results
                   ; O(2n)
        Space: O(n) ; worst case the width could be n

        '''
        val_depth = []
        depth = 1
        while nestedList:
            tmp = []
            for _ in range(len(nestedList)):
                nested = nestedList.pop()
                if nested.isInteger():
                    val_depth.append((nested.getInteger(), depth))
                else:
                    tmp.extend(nested.getList())

            nestedList = tmp
            depth += 1

        return sum(val * (depth - height) for val, height in val_depth)

        '''
        sumOfElements - sumOfProducts
        - single pass BFS
        -  slight improvement
        '''

        # val_depth = []
        # depth = 1
        # sumOfElements, sumOfProducts = 0, 0
        # while nestedList:
        #     tmp = []
        #     for _ in range(len(nestedList)):
        #         nested = nestedList.pop()
        #         if nested.isInteger():
        #             sumOfElements += nested.getInteger()
        #             sumOfProducts += (nested.getInteger() * depth)
        #         else:
        #             tmp.extend(nested.getList())

        #     nestedList = tmp
        #     depth += 1

        # return depth * sumOfElements - sumOfProducts
