# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # two pointers search: both pointers start at root,
        # and we move them "towards" p and q; once their desired
        # directions differ, the current LCA is the answer.
        def searchTwoPointers(p_curr=root, q_curr=root, LCA=root):
            # not found (shouldn't happen if p, q always exist)
            if not p_curr or not q_curr:
                return None

            # if current node matches one of the targets by value, it is the LCA
            if (
                p_curr.val == p.val or p_curr.val == q.val or
                q_curr.val == p.val or q_curr.val == q.val
            ):
                return p_curr

            # start with p only
            if p_curr.val < p.val:
                if q_curr.val < q.val:
                    # both p and q are in the right subtree: move both right,
                    # and the child becomes the new LCA candidate
                    return searchTwoPointers(p_curr.right, q_curr.right, p_curr.right)
                else:
                    # p would go right, q would not: split occurs at current LCA
                    return LCA
            else:
                if q_curr.val < q.val:
                    # q would go right, p would not: split occurs at current LCA
                    return LCA
                else:
                    # both p and q are in the left subtree: move both left,
                    # and the child becomes the new LCA candidate
                    return searchTwoPointers(p_curr.left, q_curr.left, p_curr.left)

            return LCA  # fallback, not really reached

        return searchTwoPointers(root, root, root)
