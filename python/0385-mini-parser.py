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
'''
[123,[456,[789]]]
[
    NestedInteger(int=123), 
    NestedInteger(list=[
        NestedInteger(int=456), 
        NestedInteger(list=[
            NestedInteger(int=789),
        ])
    ])
]

[[1,1],2,[1,1]]
[
    NestedInteger{_integer: None, _list: [NestedInteger{_integer: 1, _list: []}, NestedInteger{_integer: 1, _list: []}]}, 
    NestedInteger{_integer: 2, _list: []}, 
    NestedInteger{_integer: None, _list: [NestedInteger{_integer: 1, _list: []}, NestedInteger{_integer: 1, _list: []}]}
]

[1,[4,[6]]]
[
    NestedInteger{_integer: 1, _list: []}, 
    NestedInteger{_integer: None, _list: [
        NestedInteger{_integer: 4, _list: []}, 
        NestedInteger{_integer: None, _list: [
            NestedInteger{_integer: 6, _list: []}
        ]}
    ]}
]

[
    NestedInteger{_integer: 123, _list: []}, 
    NestedInteger{_integer: None, _list: [
        NestedInteger{_integer: 456, _list: []}, 
        NestedInteger{_integer: None, _list: [
            NestedInteger{_integer: 789, _list: []}
        ]}
    ]}
]

- if we reach a number, 
    - collect all the numbers connected
    - if reach ","
        - add a new NestedInteger with only the int we collected
    - if reach "]"
        - add the new Nested Integer with the int we collected
        - return the current list
- if we reach an "["
    - set the current int to None
    (when we recurse back, we need to check if int is None before adding)
    - start a new NestedInteger, and recursed to get fill the list contents

where n is the length of the string
Time: O(n)
Space: O(n)
'''


class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        if s[0] != '[':
            return NestedInteger(int(s))

        self.i = 1

        def dfs():
            nested = NestedInteger()
            num = ""
            while self.i < len(s):
                if s[self.i] == "[":
                    num = ""
                    self.i += 1
                    tmp = dfs()
                    nested.add(tmp)

                elif s[self.i] == "]":
                    if num:
                        nested.add(NestedInteger(int(num)))
                    self.i += 1
                    return nested

                elif s[self.i] == ",":
                    if num:
                        nested.add(NestedInteger(int(num)))
                    num = ""
                    self.i += 1

                else:
                    # num could be negative
                    num += s[self.i]
                    self.i += 1

            return nested

        res = dfs()
        return res
