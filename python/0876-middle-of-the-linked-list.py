# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        1 pass -> slow and fast pointer
        - slow moves 1 space
        - fast moves 2 spaces
        - when fast is out of bounds, slow is the middle value

        Time: O(n)
        Space: O(1)
        '''
        dummy = ListNode(0, head)
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
