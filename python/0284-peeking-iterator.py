# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

'''
- stored the next value in a variable
- this allows us to look at the next item without moving the pointer
- when we do want to move the pointer, we need to update the current variable value and then return
the previous value

Time: O(1)
Space: O(1)
'''


class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.peek_val = self.iterator.next() if self.iterator.hasNext() else None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.peek_val

    def next(self):
        """
        :rtype: int
        """
        res = self.peek_val
        # update the pointer by updating the self.peek_val
        self.peek_val = self.iterator.next() if self.iterator.hasNext() else None

        return res

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.peek_val:
            return True
        return False


# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
