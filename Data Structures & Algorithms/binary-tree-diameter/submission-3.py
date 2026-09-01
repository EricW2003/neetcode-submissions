# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diam = 0
        def aux(tree):
            nonlocal diam
            if not tree:
                return 0

            a , b = aux(tree.left), aux(tree.right)
            if a + b > diam:
                diam = a + b
            return max(a ,b)+1
        aux(root)
        return diam



            

    