# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        '''
        - pointers:
            - a trailing pointer, leave the pointer at that position when we find the left node (left node - 1)
            - a pointer on the left node
            - a pointer on the node after left

        - advance all pointers until the middle pointer is on the left node

        (middle pointer on left node)
        left = 2 ; right = 4
        1 - 2 - 3 - 4 - 5
        |   |   |
        curr.next = forw.next (2 -> 4)
        forw.next = prev.next (3 -> 2)
        prev.next = forw (1 -> 3)

        #advance
        forw = curr.next

        - Stopping point is when prev.next.val == right

        Time: O(n)
        Space: O(1)
        '''
        dummy_head = ListNode(0, head)
        prev, curr, forw = dummy_head, dummy_head.next, dummy_head.next.next

        left_counter = 1
        # get the pointers to the positions to start reversing
        while curr.next and left_counter != left:
            prev = prev.next
            curr = curr.next
            forw = forw.next

            left_counter += 1

        right_counter = left_counter
        # reverse portion of linked list betweent left and right
        while curr.next and right_counter != right:
            curr.next = forw.next
            forw.next = prev.next
            prev.next = forw

            # advance
            forw = curr.next
            right_counter += 1

        return dummy_head.next
