# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # reach end node, and calculate height left, height right to dismiss the repeated work...
        def height(root):
            if not root:
                return 0
            height_left = 0 # no nodes
            height_right = 0 # no nodes
            if root.left:
                height_left = height(root.left)
            if root.right:
                height_right = height(root.right)
            if height_left == -1 or height_right == -1 or abs(height_right - height_left) > 1:
                return -1
            return max(height_left, height_right) + 1
        if height(root) == -1: # how to check if it is an int return value and not boolean?
            return False
        return True