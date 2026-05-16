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
                return 0, float("-inf")  # no valid non-empty path here

            left_max, left_max_split = dfs(root.left)
            right_max, right_max_split = dfs(root.right)

            # Negative downward paths should not be attached to this node.
            left_max = max(left_max, 0)
            right_max = max(right_max, 0)

            # Best path anywhere in this subtree.
            cur_max_split = max(
                left_max_split,
                right_max_split,
                root.val + left_max + right_max
            )

            # Best path extendable to parent: can choose only one side.
            cur_max = max(left_max, right_max) + root.val

            return cur_max, cur_max_split
        
        return dfs(root)[1]