# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # T: O(n)
    # S: O(n)
    def __init__(self, head: Optional[ListNode]):
        self.lst = []
        while head:
            self.lst.append(head.val)
            head = head.next

    # T: O(1)
    def getRandom(self) -> int:
        return random.choice(self.lst)


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
