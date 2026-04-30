# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    """
    NeetCode's DFS (preorder) solution with inline comments.

    Core idea from the video:
    - Serialize: do a preorder traversal (root, left, right).
      For every real node, record its value.
      For every null child, record a special marker "N".
      Join everything with commas into one string.
    - Deserialize: read that list in the SAME preorder with a pointer i.
      At each step:
        * if vals[i] == "N": this is a null child → return None and advance i.
        * otherwise: create a node with vals[i], advance i, then recursively
          build its left subtree, then its right subtree.
    - This is correct because each pointer (child) in the tree corresponds
      to exactly one token (either a value or "N"), so the encoding is
      unambiguous and the recursive decoder mirrors the encoder.
    """

    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []  # will hold the preorder tokens (values and "N")

        def dfs(node: Optional[TreeNode]) -> None:
            """
            Preorder DFS:
            - Visit node.
            - Recurse on left.
            - Recurse on right.

            For each node:
            - If it's None, append "N" and return (base case).
            - Otherwise, append its value, then process its children.
            """
            if not node:
                # Null child: record "N" so we know this branch ends here.
                res.append("N")
                return

            # Non-null node: record its value as a string.
            res.append(str(node.val))

            # Recurse on left subtree (its encoding immediately follows the value).
            dfs(node.left)
            # Then recurse on right subtree.
            dfs(node.right)

        # Kick off DFS from the root.
        dfs(root)

        # Join tokens with commas into a single string representation.
        return ",".join(res)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        """
        Inverse of serialize.

        Steps:
        - Split the string by commas to get the token list `vals`.
        - Use an index `self.i` to walk through vals exactly once.
        - Define a recursive dfs() that:
            * reads vals[self.i],
            * either returns None (if "N") or builds a node (if a value),
            * then recursively builds left and right subtrees.
        - The recursion order (node, left, right) matches serialization order,
          so we reconstruct the same tree structure.
        """
        vals = data.split(",")  # tokens in preorder (values + "N")
        self.i = 0  # global pointer into vals, shared across recursive calls

        def dfs() -> Optional[TreeNode]:
            """
            Rebuild one subtree rooted at the current token index self.i.

            Invariant:
            - On entry, vals[self.i] is the token for the root of *this* subtree.
            - On exit, self.i has been advanced past all tokens used by this subtree.
            """
            # Base case: "N" means this subtree is empty.
            if vals[self.i] == "N":
                self.i += 1  # consume this "N"
                return None

            # Otherwise, vals[self.i] is an integer value for a real node.
            node = TreeNode(int(vals[self.i]))
            self.i += 1  # consume the value token

            # Recursively build the left subtree.
            # Because serialization was preorder, the left subtree encoding
            # starts immediately after this node's value.
            node.left = dfs()

            # After the left subtree is completely read, self.i now points
            # to the start of the right subtree tokens.
            node.right = dfs()

            # Return the root of the reconstructed subtree.
            return node

        # Rebuild the whole tree starting at index 0.
        return dfs()
