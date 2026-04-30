# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def is_valid(root, min_val = -float('inf'), max_val = float('inf')):
            if not root:
                return True
            # check if both left and right is BST
            is_left, is_right = True, True
            if root.left:
                is_left = is_valid(root.left, min_val, max_val = root.val)
            if root.right:
                is_right = is_valid(root.right, root.val, max_val)

            return min_val < root.val < max_val and is_left and is_right
        return is_valid(root)
    