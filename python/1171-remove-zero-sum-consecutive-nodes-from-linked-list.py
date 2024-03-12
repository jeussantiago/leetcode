# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        [1,2,3,-3,4]
        [1,0,0, 0,0] +1
        [3,2,0, 0,0] +2
        [6,5,3, 0,0] +3
        [3,2,0, -3,0] +(-3)
        -> [3,2,-inf,-inf,0] 
        [7,6,-inf,-inf,4]  +4

        [1,2,3,-3,-2]
        [1,0,0, 0,0] +1
        [3,2,0, 0,0] +2
        [6,5,3, 0,0] +3
        [3,2,0, -3,0] +(-3)
        -> [3,2,-inf,-inf,0]
        [1,0,-inf,-inf,-2] +(-2)
        -> [1,-inf,-inf,-inf,-inf]

        Time: O(n^2)
        Space: O(n)
        '''
        N = 1
        dp = []
        dummy = head
        # figure out which node is staying
        while dummy:
            dp.append(0)

            isConsecZero = False
            for i in range(N):
                dp[i] += dummy.val

                if dp[i] == 0:
                    isConsecZero = True

                if isConsecZero:
                    dp[i] = float('inf')

            # print(dp)
            dummy = dummy.next
            N += 1

        # create the result linked list
        dummy_head = dummy = ListNode(0)
        ind = 0
        while head:
            if dp[ind] != float('inf'):
                dummy.next = ListNode(head.val)
                dummy = dummy.next

            head = head.next
            ind += 1

        return dummy_head.next
