# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        '''
        2 pointers
        - slow and a fast to find the mid point
        -> 1 pointer at the head
        -> 1 pointer at the midpoint

        - reverse the contents after the midpoint
            1,2,2,1

            1 -> 2 -> 2 -> 1
            None <- 1 | 2 -> 2 -> 1
            None <- 1 <- 2 | 2 -> 1

            - reverse the direction of the pointers

            prev = None
            tmp = slow.next
            slow.next = prev

            prev = slow
            slow = tmp



        - you just run the algoritm normally and compare the positions for the pointers

        Time: O(n)
        Space: O(1)
        '''
        # find midpoint
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second half
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev

            prev = slow
            slow = tmp

        # compare
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        '''
        Time: O(n)
        Space: O(n)
        '''
        lst = []
        while head:
            lst.append(head.val)
            head = head.next

        return lst == lst[::-1]
