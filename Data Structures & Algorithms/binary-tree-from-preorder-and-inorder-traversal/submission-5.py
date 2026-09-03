# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #preorder root left right
        #inorder left root right

        dic = {inorder[i]:i for i in range(len(inorder))}

        def dfs(pre_low,pre_high,in_low,in_high):
            if pre_low==pre_high: return None
            root = preorder[pre_low]
            # n_root = 0
            # while inorder[in_low+n_root]!=root and n_root<(in_high-in_low):
            #     n_root+=1
            n_root = dic[root]-in_low
            return TreeNode(root,dfs(pre_low+1,pre_low+n_root+1,in_low,in_low+n_root),dfs(pre_low+n_root+1,pre_high,in_low+n_root+1,in_high))
        
        return dfs(0,len(preorder),0,len(preorder))


            
            
        