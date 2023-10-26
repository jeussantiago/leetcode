# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def correctBinaryTree(self, root: TreeNode) -> TreeNode:
        '''
        BFS

        - since all the node values are unique, we can store all the existing
        node values from the row in a set
        - each node will also store its parent and the direction(left or right)
            - so that if we find the incorrectly pointer node, we can 
            set the parents child to empty node

        Note:
            - its always the right child that points to a wrong node
            - all nodes are unique

        n is the total number of nodes
        Time: O(n)
        Space: O(n)
            ; hashset will have all the visited node values

        q = [4, 2]
        row_exist = set(3, 1, 7, 9, 4, 2)
        '''
        # curr_node, parentNode, isLeftChild
        q = collections.deque([(root, None, True)])
        issue_node_parent = None
        issue_node_isLeftChild = None
        row_exist = set()
        while q:
            for _ in range(len(q)):
                currNode, parentNode, isLeftChild = q.pop()

                # check if right child is in row
                if currNode.right and currNode.right.val in row_exist:
                    # found the issue node
                    issue_node_parent = parentNode
                    issue_node_isLeftChild = isLeftChild
                    break

                # add children to queue
                if currNode.left:
                    q.appendleft((currNode.left, currNode, True))
                    row_exist.add(currNode.left.val)
                if currNode.right:
                    q.appendleft((currNode.right, currNode, False))
                    row_exist.add(currNode.right.val)

        if issue_node_isLeftChild:
            issue_node_parent.left = None
        else:
            issue_node_parent.right = None

        return root
