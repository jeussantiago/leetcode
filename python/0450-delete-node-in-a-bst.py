# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        '''
        - find the key
            - since it's a bst, we can go left or right depending if the curretn value is smaller or larger than key

        if node doesn't have any kids
            - return None

        if node doesnt have left child
            - return the right child

        if node doesn't have right child
            - return left

        node has 2 kids:
            - just go to the right subtree and get the smallest value
            - replace the current node with the smallest value

            - remove the that smallest value
            - the smallest value if a leaf node with no kids so we can just call this same function 
            with a new key=leaf_node_val

        h is the height of the binary tree
        Time: O(h)
            ; the time complexity could be (n) since the tree could be skewed to one side but avg is (h)
        Space: O(1)
        '''
        if not root:
            return root

        if key < root.val:
            root.left = self.deleteNode(root.left, key)

        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        else:
            # leaf node
            if not root.left and not root.right:
                return None

            elif not root.left:
                return root.right

            elif not root.right:
                return root.left

            else:
                # 2 kids
                node = root.right
                while node.left:
                    node = node.left
                root.val = node.val

                root.right = self.deleteNode(root.right, root.val)

        return root
