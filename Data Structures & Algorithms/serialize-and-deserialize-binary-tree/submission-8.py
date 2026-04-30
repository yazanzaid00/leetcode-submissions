# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    def serialize(self, root):
        if not root:
            return "N"
        res = []
        q = deque([root])
        while q:
            node = q.popleft()
            if not node:
                res.append("N")
            else:
                res.append(str(node.val))
                q.append(node.left)   # may be None
                q.append(node.right)  # may be None
        return ",".join(res)

    def deserialize(self, data):
        vals = data.split(",")
        if vals[0] == "N":
            return None

        root = TreeNode(int(vals[0]))
        q = deque([root])
        i = 1
        while q:
            node = q.popleft()

            # Left child
            if vals[i] != "N":
                node.left = TreeNode(int(vals[i]))
                q.append(node.left)
            i += 1

            # Right child
            if vals[i] != "N":
                node.right = TreeNode(int(vals[i]))
                q.append(node.right)
            i += 1

        return root
