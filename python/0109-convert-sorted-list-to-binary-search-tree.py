# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        '''
        Solution 1:
        (sapce inefficient b/c we store the list in a array)
        - convert list to array
        - create bst out of array

        Solution 2:
        - we still need to know the length of the linked list
        - since the linked list is in ascending order, we know that this number will be at the very bottom left of the tree
        - we also know that with inorder traversal, we can go to the very bottom left before adding/looking at a node

        - traverse the tree like binary search, using mid points as the stopping point
        - go left all the way to the bottom left
        - the mid points, start and ends will help decide when to stop going left or right
        - -10 point to none
        - recurse back and passes the node -10 to 'left'
        - creates node(-3)
        node(-3).left = left (which is the node(-10))
        -  recurse back and does it again for 0

        - this is based on the traversal of the mid like binary search

        Time: O(n)
        Space: O(n)
        '''

        # Solution 2:
        curr = head
        N = 0
        while curr:
            N += 1
            curr = curr.next

        def helper(left, right):
            nonlocal head
            if left > right:
                return

            mid = (left + right) // 2
            # traverse left
            left = helper(left, mid-1)
            node = TreeNode(head.val)
            head = head.next
            node.left = left
            # traverse right
            node.right = helper(mid+1, right)

            return node

        return helper(0, N-1)
