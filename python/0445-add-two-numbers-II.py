# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        n is length of l1
        m is length of l2
        Time: O(max(m, n))
            ; (n) reverse l1
            ; (m) reverse l2
            ; (max(m, n)) create additive solution
            ; (max(m, n)) reverse solution
        Space: O(max(m, n))
        '''

        def reverseLinkedList(node):
            prev = None
            while node:
                tmp = node.next
                node.next = prev
                prev = node
                node = tmp
            return prev

        l1 = reverseLinkedList(l1)
        l2 = reverseLinkedList(l2)
        # [8,8,2,7]
        # [8,8,5]

        root = ListNode(0)
        node = root
        carry = 0
        while l1 or l2 or carry:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            node_val = l1_val + l2_val + carry
            carry = node_val // 10
            node_val = node_val % 10

            node.next = ListNode(node_val)
            node = node.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return reverseLinkedList(root.next)
