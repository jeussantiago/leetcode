# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        1) number of nodes in linked list between 0 and 50
        2) value of node between -100 and 100
        3) both provided linked list already sorted in increasing order

        1. go through both linked list
        2. compare which number is greater (if both values are the same, we can use whichever list)
        3. append that node to the next value in the linked list we create (dummy_head)
        4. advance the node which was appened


        Time: O(m+n) where m and n are the size of the lists
        Space: O(m+n) where m and n are the size of the lists
        '''
        #head of dummy
        dummy_head = ListNode()
        #iterator of dummy
        dummy = dummy_head

        while list1 != None and list2 != None:
            #list1 is greater
            if list1.val <= list2.val:
                dummy.next = list1
                list1 = list1.next
            else:
                dummy.next = list2
                list2 = list2.next
            dummy = dummy.next
        #leftover nodes
        if list1:
            dummy.next = list1
        elif list2:
            dummy.next = list2
            
        return dummy_head.next