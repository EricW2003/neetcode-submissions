# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root: return True

        def dfs(node,low,end):
            if not node: return True

            l , r = node.left, node.right

            return (low<node.val<end) and dfs(l,low,node.val) and dfs(r,node.val,end)
            
        return dfs(root,float("-inf"),float("inf"))
