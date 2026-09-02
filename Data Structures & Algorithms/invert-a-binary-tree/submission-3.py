# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None: return None
        stack = [root]
        def dfs():
            a = stack.pop()
            if a.left is not None:
                stack.append(a.left)
                dfs()
            if a.right is not None:
                stack.append(a.right)
                dfs()
            a.left, a.right = a.right, a.left
        dfs()
        return root