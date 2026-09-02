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
                if n not in dic:
                    dic[n] = [node.val]
                else:
                    dic[n].append(node.val)
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
            n+=1
        ans = []
        for i in range(n):
            ans.append(dic[i])
        return ans
