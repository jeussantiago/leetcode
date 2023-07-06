# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        '''
        1-2-3-4-5 k = 4
        - get kth node -> node: 4
        - pointer on kth.next -> node:5
        - pointer on last node previous of group -> node: 0

        1) have 2 updating node
            - first being the first position of the group
                node: 1
            - second being the second position of the group
                node: 2
            1-2-3-4-5
        2) set first position.next equal to kth.next
            1-2-3-4-5 => 1-5
        3) set kth.next equal to the moved first position
            1-2-3-4-1-5
        4) set previous of Group node.next equal to second node
            0-2-3-4-1-5
        5) repeat until curr first position node is equal to the kth node
            0-2-3-4-1-5
            0-3-4-2-1-5
            0-4-3-2-1-5

        6) set prevGroupNode to first position, set

        Time: O(n)
        Space: O(1)
        '''
        dummy = ListNode(0, head)
        groupPrevNode = dummy

        while True:
            kthNode = self.getKthNode(groupPrevNode, k)
            if not kthNode:
                break
            first, nextGroupNode = groupPrevNode.next, kthNode.next
            #the very first position for the next group
            prevNextGroupNode = first
            while first != kthNode:
                second = first.next
                first.next = kthNode.next
                kthNode.next = first
                groupPrevNode.next = second

                first = groupPrevNode.next
            #advance pointer
            groupPrevNode = prevNextGroupNode

        return dummy.next



    def getKthNode(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr


