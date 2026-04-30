# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parent = defaultdict(TreeNode)
        level = defaultdict(int)
        # BFS
        curr_level = 0
        queue = deque([root])
        parent[root] = None
        while queue:
            for _ in range(len(queue)):
                curr_node = queue.popleft()
                # node.val is unique so they are good keys, idecieed by end to even take the curr node as a key is better..
                level[curr_node] = curr_level
                if curr_node.left:
                    parent[curr_node.left] = curr_node
                    queue.append(curr_node.left)
                if curr_node.right:
                    parent[curr_node.right] = curr_node
                    queue.append(curr_node.right)
            curr_level += 1

        while level[p] < level[q]:
            q = parent[q]
        while level[q] < level[p]:
            p = parent[p]
        # now p and q are pn the same level

        while level[q] and level[p] and q != p:
            q = parent[q]
            p = parent[p]
        return q
