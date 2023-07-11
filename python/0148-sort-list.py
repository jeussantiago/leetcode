# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Solution 2:
        - impelment mergesort
        - get the mid point
        - split the linked list into 2 seperate list (recursively)

        Merge the 2 list:
        - mergsort works because it each list is sorted when you merge them together
        -1 5 
        3
        4 0
        - while left list and right list both have values
        - if left val is < right val:
            - add the left value to the end of list
            - move the left value to next
        - lef val grater > right val;
            - add right val to end of list
            - move right value over
        - move current list pointer over

        - at this point, 1 of the 2 list is going to still have values
        - have the cur.next = list1 or list2 (whichever is not null anymore)
        -1 3 5
        4 0
        - then combine these 2 order list already

        Time: O(nlogn)
        Space: O(n)
        '''
        if not head or not head.next:
            return head

        # get the midNode
        midNode = self.getMidPoint(head)

        # split the list until theres only 1 left in the list
        leftNode = self.sortList(head)
        rightNode = self.sortList(midNode)

        return self.mergeSort(leftNode, rightNode)

    # get the mid node of a linked list
    def getMidPoint(self, head):
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        # split the linked list into 2 seperate list
        midNode = slow.next
        slow.next = None
        return midNode

    def mergeSort(self, list1, list2):
        dummy = ListNode()
        cur = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next

        # either list1 or list2 will still have values, stick it
        # to the end of the list
        cur.next = list1 or list2
        return dummy.next
