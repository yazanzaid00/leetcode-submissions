# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        # pre order build
        def preorder(root, res):
            if root is None:
                res.append(f"{root}#")
                return
            res.append(f"{root.val}#")
            preorder(root.left, res)
            preorder(root.right, res)
        preorder(root, res)
        return "".join(res)
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        def build_from_preorder(nodes_vals):
            nonlocal index
            if nodes_vals[index] == "None":
                index += 1
                return None
            curr_node = TreeNode(int(nodes_vals[index]), None, None)
            index += 1
            curr_node.left = build_from_preorder(nodes_vals)
            curr_node.right = build_from_preorder(nodes_vals)
            return curr_node
        index = 0
        nodes_vals = data.split('#')
        return build_from_preorder(nodes_vals)
