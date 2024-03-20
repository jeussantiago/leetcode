# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        '''
        Time: O(n + m)
        Space: O(1)
        '''

        a -= 1  # node we want to keep is the node before node a
        b += 1  # node we want to keep is the node after node b

        # split list1
        left = right = None
        dummy = list1
        curr_ind = 0
        while dummy:
            if curr_ind == a:
                left = dummy
            elif curr_ind == b:
                right = dummy

            dummy = dummy.next
            curr_ind += 1

        # get a pointer on the last node on list2
        list2_last_node = list2
        while list2_last_node.next:
            list2_last_node = list2_last_node.next

        # combine the list parts together
        left.next = list2
        list2_last_node.next = right

        return list1
