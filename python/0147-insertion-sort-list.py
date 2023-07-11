# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''

        - start a second List with the value of the first node in head
        - move head to its next
        - loop through head until its none
            - to find its rightful place in second List -> 
            traverse second list until 
            (current first list node val is < than second list node val or
            cur.next == None)

        4 2 1 3
        0 2 4

        Time: O(n^2)
        Space: O(n)
        '''
        second = ListNode()
        cur = head

        while cur:
            sec = second
            # find the right position for current number
            while sec.next and (cur.val > sec.next.val):
                sec = sec.next

            tmp = cur.next
            cur.next = sec.next
            sec.next = cur
            cur = tmp

        return second.next
