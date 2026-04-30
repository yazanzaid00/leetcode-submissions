# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(current_root, current_subroot):
            if not current_root or not current_subroot:
                return not current_root and not current_subroot
            return current_root.val == current_subroot.val and isSameTree(current_root.left, current_subroot.left) and isSameTree(current_root.right, current_subroot.right)
        
        stack = []
        current = root
        while stack or current:
            while current:
                stack.append(current)
                current = current.left
            # Check If they are the same tree
            current = stack.pop()
            if (isSameTree(current, subRoot)):
                return True
            current = current.right
        return False
            