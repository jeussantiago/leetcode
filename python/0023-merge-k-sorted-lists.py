# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        '''
        1) array of linked lists
        2) node value between -10^4 and 10^4

        1. merge 2 linked list is sorter acending order
        2. iterate through current list
        3. sort/compare 2 linked lit with each other, i and i+1
        4. save in a new array and repeat step 3 until theres only 1 array left

        [[1,4,5],[1,3,4],[2,6]] -> [[1,1,3,4,4,5],[2,6]] -> [[1,1,2,3,4,4,5,6]] 
        
        idea similar to merge sort

        5 - 7 - 3 - 8 
        5,7 - 3,8           O(n) to sort 5 and 7
        3,5,7,8             O(n) to sort the 4 nodes
                            taking our lists and dividing by 2
                            log(k) is the number of times we repeat the O(n) step to sort

        Time: O(nlog(k)) where n is the length of individual linked lists and k is the number of linked list

        '''
        if len(lists) == 0:
            return None

        while len(lists) > 1:
            mergedKList = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None
                newMergedList = self.mergeTwoLists(l1, l2)
                mergedKList.append(newMergedList)
            lists = mergedKList

        return lists[0]
        

        
    def mergeTwoLists(self, l1, l2):
        dummy_head = ListNode()
        dummy = dummy_head

        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                dummy.next = l1
                l1 = l1.next
            else:
                dummy.next = l2
                l2 = l2.next
            dummy = dummy.next
        #any leftovers in linked list
        if l1:
            dummy.next = l1
        elif l2:
            dummy.next = l2
        return dummy_head.next
