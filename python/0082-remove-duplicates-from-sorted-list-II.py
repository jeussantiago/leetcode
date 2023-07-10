# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        3 pointers
        - stay at the node with the number before the current number
        - 2 pointers to test whether a number repeated
            - curr == forw
                - continuosly increaes forward until forward.next != forward
                    -> prev.next = forward.next
                    curr = forward.next
                    forward = curr.next
            - else:
                #numbers not repeating so we can just continuosly increase the pointers
                prev = prev.next
                crr = curr.next
                forw = forw.next 

        Time: O(n)
        Space: O(1)
        '''

        if not head:
            return head
        dummy_head = ListNode(0, head)
        prev, forw = dummy_head, dummy_head.next

        while forw != None:
            if forw.next and forw.val == forw.next.val:
                # advance forward pointer to remove all instances of the repeating number
                while forw.next and forw.val == forw.next.val:
                    forw = forw.next
                prev.next = forw.next
            else:
                prev = prev.next

            forw = forw.next

        return dummy_head.next
