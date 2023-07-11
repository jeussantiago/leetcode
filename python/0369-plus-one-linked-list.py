# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        '''
        - a number 123 is stored in a linked list
        - just add +1 to the number 
            - but since its a linked list you have to traverse and change the previous numbers if needed

        - simple case : 123 => 124
        - moderate case : 129 => 130
        - annoying case : 999 => 1000
        - another case: 192 => 193

        - can have a dummy node with val=0 pointing to the head just in case for the annoying
        - iterate until we find a 9
            - but another case is if 9 is in the middle like 192, so we need to iterate through the entire linked list
            - if the val != 9 we can update the pointer

        - once iteration is finished, we can just increase the val of the non-9 pointer and turn every number after it to zero

        - the dummy node will be 0 or 1 at the end so return base on those values

        Time: O(2n) 
            : O(n)
        Space: O(1)
        '''

        dummy_head = ListNode(0, head)
        curr = dummy_head
        non_nine = None

        # get the rightmost non 9 number
        while curr:
            if curr.val != 9:
                non_nine = curr
            curr = curr.next

        # increase teh val of the non 9 pointer and turn every number after it to 0
        non_nine.val += 1
        non_nine = non_nine.next
        while non_nine:
            non_nine.val = 0
            non_nine = non_nine.next

        if dummy_head.val == 1:
            return dummy_head
        return dummy_head.next
