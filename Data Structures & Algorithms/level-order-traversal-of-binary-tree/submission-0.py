# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # BFS traversal
        if not root:
            return []
        queue = deque()
        queue.append(root)
        result =  []
        while queue:
            level = []
            for _ in range(len(queue)):
                curr_node = queue.popleft()
                if curr_node:
                    level.append(curr_node.val)
                    queue.append(curr_node.left)
                    queue.append(curr_node.right)
            if level:
                result.append(level)
        return result