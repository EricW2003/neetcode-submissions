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

        dic = {}
        q = deque([root])
        n=0
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                val = node.val
                if n not in dic:
                    dic[n] = [val]
                else:
                    dic[n].append(val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            n+=1
        ans = []
        for i in range(n):
            ans.append(dic[i])
        return ans
