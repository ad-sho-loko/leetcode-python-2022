# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution104:
    def maxDepth(self, root: TreeNode) -> int:
        def traverse(node: TreeNode, depth: int) -> int:
            if not node: return depth
            l = traverse(node.left, depth + 1)
            r = traverse(node.right, depth + 1)
            return max(l, r)

        return traverse(root, 0)
