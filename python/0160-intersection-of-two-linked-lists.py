# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        '''
        - one of the list is longer than the other
        - if you traverse through one list then traverse through the other
        list when you reach the end, you can meet up with the reciprocate
        - if they don't meet up at any node, they will both be on the null
        node at the very end, in that case the answer is null

        Time: O(m + n)
        Space: O(1)
        '''
        l1, l2 = headA, headB
        while l1 != l2:
            l1 = l1.next if l1 else headB
            l2 = l2.next if l2 else headA
        return l1
