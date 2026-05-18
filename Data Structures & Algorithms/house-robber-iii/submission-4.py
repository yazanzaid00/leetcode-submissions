# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return 0, 0
            left_taken, left_skip = dfs(root.left)
            right_taken, right_skip = dfs(root.right)

            best_taken = left_skip + right_skip + root.val
            best_skip = max(left_taken, left_skip) + max(right_taken, right_skip) 

            return best_taken, best_skip
        return max(dfs(root))