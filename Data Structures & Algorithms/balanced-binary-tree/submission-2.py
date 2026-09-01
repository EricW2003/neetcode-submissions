# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def height(tree):
    if not tree:
        return -1
    return max(height(tree.left),height(tree.right))+1

def verification(tree):
    if not tree:
        return True
    h1 = height(tree.left)
    h2 = height(tree.right)
    return (h1-h2)**2<2
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return verification(root) and verification(root.left) and verification(root.right)







