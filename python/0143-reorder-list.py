# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.

        Solution 2 (doesn't use other data structures and doesn't use extra memory):
        - get mid point of list
        1,2,3,4,5,6,7
              ^
             mid

        - reverse second half
        1,2,3,4
        7,6,5

        - merge both sides of list
        1,7 - 2,6 - 3,5 - 4

        Time: O(n)
        Space: O(1)
        """
        # SOLUTION 2

        if not head:
            return []

        # get mid of linked list
        slow, fast = head, head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        mid_node = slow
        # reverse second half
        prev, cur = None, mid_node.next
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        mid_node.next = None

        # merge both sides
        first, second = head, prev
        while second:
            tmp = second.next
            second.next = first.next
            first.next = second
            first = second.next
            second = tmp

        return head


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.

        stack:
        - append everything to a stack

        Creating new order:
        - popLeft
        - then pop to get the other end of the stack


        Time: O(n)
        Space: O(n)
        """

        dummy = ListNode(0, head)
        cur = dummy.next
        q = collections.deque()

        while cur:
            q.append(cur)
            cur = cur.next

        cur = dummy
        rightSide = False
        while q:
            node = q.pop() if rightSide else q.popleft()
            node.next = None
            cur.next = node
            cur = cur.next
            rightSide = not rightSide

        return head
