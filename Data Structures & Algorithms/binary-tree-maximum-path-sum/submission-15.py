# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(root: Optional[TreeNode]) -> Tuple[int, int]:
            if not root:
                return 0, -float("inf") 
            
            left_max_down, left_max = dfs(root.left)
            right_max_down, right_max = dfs(root.right)

            cur_max = max(left_max, right_max, left_max_down + right_max_down + root.val, left_max_down + root.val,  right_max_down + root.val, root.val)
            cur_max_down = max(left_max_down + root.val, right_max_down + root.val, root.val) 
            return cur_max_down, cur_max
        return dfs(root)[1]