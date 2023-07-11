# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        '''
        - method works below
        - but since this problem states that it will never be the last node, we can do something efficient

        - make the current node, take the next nodes value
        - since the current node is pretty much a copy of the next value, we can get rid of the next value
        Time: O(1)
        Space: O(1)
        '''
        node.val = node.next.val
        node.next = node.next.next


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.

        - swap current node value with the value of the next


        Time: O(n)
        Space: O(1)
        """

        prev = ListNode(0, node)
        while node.next:
            node.val, node.next.val = node.next.val, node.val
            node = node.next
            prev = prev.next

        prev.next = None
