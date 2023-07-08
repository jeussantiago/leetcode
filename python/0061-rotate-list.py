# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        '''
        Solution 2:
        - get length of inkedlist for same reason
        - make linked list circular
        - have a k step behind pointer
        - return the k step pointer as results
        Time: O(n)
        Space: O(1)
        '''
        if not head or not head.next : return head

        curr = head
        N = 1
        while curr.next:
            N += 1
            curr = curr.next
        #make into circular linked list
        curr.next = head

        k = N - k % N
        curr = head
        cnt = 0
        while cnt < k:
            prev = curr
            curr = curr.next
            cnt += 1
        #can't see linked list while it is a circular linekd list - have to set an end
        prev.next = None
        head = curr
        return head

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        '''
        - get the length of the linkedlist
        (k might be greater than the length so it would a waste of time to constantly rotate repeatedly)
        - need a previous pointer that is k steps behind of the original pionter
            - point forward pointer to head 1-2-3-4-5-1-2-3
            - point head to prev ponter

        Time: O(n + n) where n is the length of the linked list
            : O(n)
        Space: O(1)
        '''

        if not head or not k: return head

        N = 0 #length of the linked list
        dummy_head = ListNode(0, head)
        dummy = dummy_head

        #get the length of the linked list
        while dummy.next != None:
            N += 1
            dummy = dummy.next
        # modified rotation of k
        k = k % N
        # if the length of the linked list is 1, then no matter how many times you roate, it will be the same - same thing with k = 0
        if N == 1 or not k: return head

        dummy, prev_pointer, forward_pointer = dummy_head.next, dummy_head, dummy_head
        
        #move the pointers to k length before the end
        cnt = 0
        while forward_pointer.next != None:
            if cnt == k:
                prev_pointer = prev_pointer.next
            else:
                cnt += 1
            forward_pointer = forward_pointer.next

        #rotate list
        dummy_head.next = prev_pointer.next
        prev_pointer.next = None
        forward_pointer.next = dummy

        return dummy_head.next





        