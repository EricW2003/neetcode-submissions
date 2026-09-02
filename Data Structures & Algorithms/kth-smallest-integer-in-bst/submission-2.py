# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = []
        n = 0

        def dfs(node):
            if not node: return
            dfs(node.left)
            nonlocal n
            if n<k:
                n+=1
                ans.append(node.val)
            if n<k:
                dfs(node.right)
        dfs(root)
        
        return ans[-1]
