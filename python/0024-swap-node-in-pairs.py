# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        1) number of nodes can be zero to 100
        2) previous and forward pointer


        1-2-3-4
        0-1-2-3-4 (4 pointers on 0,1,2,3)
        0-2-3-4   (point first pointer to third pointer)
        0-2-1-2-3-4 (point third pointer to second pointer)
        0-2-1-3-4 (pointer second pointer to fourth pointer)
        Finished swapping - advance pointers
        - first pointer takes node of second pointer (because of swapping)
        - second pointer takes node of fourth pointer (because of swapping)

        Time: O(n)
        '''

        dummy = ListNode(0, head)
        prev, curr = dummy, head

        while curr and curr.next:
            third = curr.next
            fourth = curr.next.next
            
            prev.next = third
            third.next = curr
            curr.next = fourth

            prev = curr
            curr = fourth

        return dummy.next