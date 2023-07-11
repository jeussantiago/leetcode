# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        - 2 pointers
            - 1 at prev
            - 1 at head
            - 1 at node we toss to the head

        prev.next = curr.next (5 -> 2)
        curr.next = head.next (3 -> 4)
        head.next = curr (0 -> 3)

        #advance
        (prev will pretty much never move since the first element is going to be the last)
        - curr = prev.next
        (then head is head)

        5 - 4 - 3 - 2 - 1
        4 - 5 - 3 - 2 - 1
        3 - 4 - 5 - 2 - 1

        Time: O(n)
        Space: O(1)
        '''

        if not head:
            return head
        dummy_head = ListNode(0, head)
        prev, curr = dummy_head.next, dummy_head.next.next

        while prev.next:
            prev.next = curr.next
            curr.next = dummy_head.next
            dummy_head.next = curr

            # advance
            curr = prev.next

        return dummy_head.next
