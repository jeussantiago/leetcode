# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        - trailing and leading pointers
        head = [2,1,3,5,6,4,7]
        l, r = head, head.next

        start_of_even = l.next
        next_odd_node = r.next
        l.next = next_odd_node
        r.next = next_odd_node.next
        next_odd_node.next = start_of_even

        l = l.next
        r = r.next

        2,1,3,5,6,4,7
        | |

        2,3,1,5,6,4,7
          |   |

        Time: O(n)
        Space: O(1)

        '''
        if not head:
            return head

        l, r = head, head.next
        while r and r.next:
            start_of_even = l.next
            next_odd_node = r.next
            l.next = next_odd_node
            r.next = next_odd_node.next
            next_odd_node.next = start_of_even

            l = l.next
            r = r.next

        return head
