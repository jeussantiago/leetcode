# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    '''
                7
        3               15
    1       2       9       20


    - initialize in constructor a stack
    - initially the first left traversals go into the stack

    next
        - pop current Node (this is the value to return)
        - go to right of current node 
            - add node top stack
            - traverse through all left nodes until no more left nodes

    '''

    def __init__(self, root: Optional[TreeNode]):
        '''
        Time: O(h)
        Space: O(h)
        '''
        self.stack = []
        self.leftTraversal(root)

    def leftTraversal(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        '''
        Time: O(h) ; avg O(1)
        Space: O(h)
        '''
        node = self.stack.pop()
        # populate the stack with the left childrens of the right node
        self.leftTraversal(node.right)
        # next number in inorder traversal
        return node.val

    def hasNext(self) -> bool:
        '''
        Time: O(1)
        Space: O(h)
        '''
        return True if self.stack else False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
