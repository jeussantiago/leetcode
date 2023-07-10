# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Time: O(n)
        Space: O(1)
        '''
        if not head:
            return head

        dummy_head = ListNode(head.val, head)
        prev, curr = dummy_head, dummy_head.next

        while curr != None:
            if prev.val == curr.val:
                prev.next = curr.next
            else:
                prev = prev.next
            curr = curr.next

        return dummy_head
