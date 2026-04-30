# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # We want to return the kth smallest...
        sorted_arr = []
        def inorder(root_help=root):
            if not root_help:
                return
            inorder(root_help.left)
            sorted_arr.append(root_help.val)
            inorder(root_help.right)
        inorder(root)
        return sorted_arr[k - 1] if k - 1 < len(sorted_arr) else None