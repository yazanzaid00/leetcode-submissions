# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValidBSTHelper(current=root, minimum=float('-inf'), maximum=float('inf')):
            if not current:
                return True
            # handle edge cases:
        
            if current.left and current.right:
                return minimum < current.val < maximum and isValidBSTHelper(current.left, minimum, current.val) and isValidBSTHelper(current.right, current.val, maximum)
            if current.left:
                return minimum < current.val < maximum and isValidBSTHelper(current.left, minimum, current.val)
            if current.right:
                return minimum < current.val < maximum and isValidBSTHelper(current.right, current.val, maximum)
            return minimum < current.val < maximum
        return isValidBSTHelper()