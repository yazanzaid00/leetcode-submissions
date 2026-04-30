# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def is_valid_bst(root, min_val = -float('inf'), max_val = float('inf')):
            if not root:
                return True
            if root.val <= min_val or root.val >= max_val:
                return False
            
            return is_valid_bst(root.left, min_val, max_val=root.val) and \
            is_valid_bst(root.right, root.val, max_val)
        return is_valid_bst(root, min_val = -float('inf'), max_val = float('inf'))