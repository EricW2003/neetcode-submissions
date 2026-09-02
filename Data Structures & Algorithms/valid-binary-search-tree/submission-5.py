# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root: return True

        def dfs(node):
            if not node: return True,float("inf"),float("-inf")
            
            l , r = node.left, node.right

            l_bool,l_min,l_max = dfs(l)
            r_bool, r_min, r_max = dfs(r)

            val = node.val

            node_max = max(l_max,r_max,val)
            node_min = min(l_min,r_min,val)
            return (l_max<val) and (val<r_min) and l_bool and r_bool, node_min, node_max

        return dfs(root)[0]
