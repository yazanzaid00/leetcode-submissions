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
            
            left_root, right_root = root.left, root.right
            best_left, best_left_exclude = dfs(root.left)
            best_right, best_right_exclude = dfs(root.right)
            
            best_cur, best_cur_exclude = root.val + best_left_exclude + best_right_exclude, max(best_left, best_left_exclude) + max(best_right, best_right_exclude)
            return best_cur, best_cur_exclude
 
        return max(dfs(root))
