# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
        1) remove nth from the back
        2) atleast 1 node in linked list
        3) value of node between 0 and 100 (don't think this matters)

        1. 2 pointers delayed by n steps
        2. if reach the end, target at the previous pointer.next, is what you are looking for
             remove that target by redirecting pointer from previous pointer to current pointer

        Time: O(n) where n is the size of the linked list
        '''
        dummy_head = ListNode(0)
        dummy_head.next = head
        delayedPointer, forwardPointer = dummy_head, head
        delayCounter = 0
        while forwardPointer != None:
            forwardPointer = forwardPointer.next
            if delayCounter >= n:
                delayedPointer = delayedPointer.next
            else:
                delayCounter += 1

        delayedPointer.next = delayedPointer.next.next
        return dummy_head.next
