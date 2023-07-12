# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        '''
        reverse the first half
        5 -> 4 -> 2 -> 1
        None <- 5 , 4 -> 2 -> 1
        None <- 5 <- 4 , 2 -> 1

        Time: O(n)
        Space: O(1)
        '''
        prev, slow, fast = None, head, head
        while fast and fast.next:
            # get the mid point for the second half of the linked list
            fast = fast.next.next

            # reverse the first half
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp

        # prev is the first half/ first twin
        # slow is the second half/ second twin
        res = 0
        while slow:
            res = max(res, slow.val + prev.val)

            slow = slow.next
            prev = prev.next

        return res


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        '''
        Throw the first half in a stack
        Time: O(n)
        Space: O(n)
        '''
        # slow and fast pointer to get the mid point/forward twin
        stack = []
        fast, curr = head, head
        while fast and fast.next:
            stack.append(curr.val)

            fast = fast.next.next
            curr = curr.next

        # add up the twins
        max_twin_sum = 0
        while stack and curr:
            max_twin_sum = max(max_twin_sum, stack.pop() + curr.val)
            curr = curr.next

        return max_twin_sum
