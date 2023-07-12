# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        '''
        single pass

        - when the front node finishes, the distance from the dummy node and the end node is the exact distance (k)
        which you eed to seperate the endNode and the curretn Node, so you can just start moving that endNode

        Time: O(n)
        Space: O(1)
        '''
        i = 1
        from_beg, from_last, dummy = head, head, head

        while dummy.next:
            if i < k:
                from_beg = from_beg.next
            else:
                from_last = from_last.next

            dummy = dummy.next
            i += 1

        from_beg.val, from_last.val = from_last.val, from_beg.val

        return head
