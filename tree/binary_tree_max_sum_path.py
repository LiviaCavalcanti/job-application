"""
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.
       -10
       /  \
      9    20
          /  \
         15   7


Node	left_gain	right_gain	Bend sum	Return up
9	0	0	9	9
15	0	0	15	15
7	0	0	7	7
20	15	7	42	35
-10	9	35	34	25

Answer: 42 (path: 15 → 20 → 7)

Why return only one side? A path is a sequence of connected nodes — if you returned both sides, the parent would create a branching structure (not a valid path). The "bend" can only happen once, which is why we check it as a candidate for max_sum but don't pass it upward.

O(n) time, O(h) space (recursion stack, where h = tree height).
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxPathSum(root):
    max_sum = float('-inf')

    def dfs(node):
        nonlocal max_sum
        if not node:
            return 0

        left_gain = max(dfs(node.left), 0)   # ignore negative paths
        right_gain = max(dfs(node.right), 0)

        # Case 1: path bends here (left → node → right)
        max_sum = max(max_sum, node.val + left_gain + right_gain)

        # Case 2: return best single-side path to parent
        return node.val + max(left_gain, right_gain)

    dfs(root)
    return max_sum

