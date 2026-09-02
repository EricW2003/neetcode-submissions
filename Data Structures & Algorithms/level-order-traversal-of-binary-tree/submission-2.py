# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: return []

        dic = []
        q = deque([root])
        n=0
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                val = node.val
                if n >=len(dic):
                    dic.append([val])
                else:
                    dic[n].append(val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            n+=1
        return dic
