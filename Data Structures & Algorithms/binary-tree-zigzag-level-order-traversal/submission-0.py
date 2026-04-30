# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        # bfs solves this easily by level
        queue = deque()
        queue.append(root)
        # while it is not empty
        while queue:
            level = []
            for _ in range(len(queue)):
                curr_node = queue.popleft()
                level.append(curr_node.val)
                # add its children
                if curr_node.right:
                    queue.append(curr_node.right)
                if curr_node.left:
                    queue.append(curr_node.left)   # or pushright syntax thing

            if len(res) % 2:
                res.append(level)
            else:
                res.append(level[::-1])# or use reveresed

        return res
