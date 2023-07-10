# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        '''
        - find first instance of a number (< x) -> first pointer
        - second pointer to go through the linked list

        0 1 4 3 2 5 2

        - if number < x: add it to one list
        - if number >= x: add to another list

        end of loop
        - combine both list
        - set end to 0


        Time: O(n)
        Space: O(n)
        '''

        lesser_head = lesser = ListNode(0)
        greater_head = greater = ListNode(0)

        while head:
            if head.val < x:
                lesser.next = head
                lesser = lesser.next
            else:
                greater.next = head
                greater = greater.next

            head = head.next

        greater.next = None
        lesser.next = greater_head.next

        return lesser_head.next
