# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #create own linked list
        root = ListNode()
        curr = root
        #numbers 10 and over need to add to the next number like normal addition (7 + 8 = 15)
        carriedNum = 0
        while l1 or l2 or (carriedNum > 0): #edge case of both list being same length but carries over
            # get the values - if linked list have different lengths then make the value 0
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            #insert into dummy linked list - carry over number
            addVal = val1 + val2 + carriedNum
            currVal = (addVal % 10) #(Ex: 7 % 10 = 7, 15 % 10 = 5)
            carriedNum = addVal // 10 #(Ex: 7 // 10 = 0, 15 % 10 = 1)
            curr.next = ListNode(currVal) #create new node with added value
            # print(addVal, carriedNum, currVal)
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            curr = curr.next

        print(root.next)
        return root.next

        