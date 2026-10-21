"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        dic = {}

        visited_node = set()

        def dfs(x):
            if not x or x.val in visited_node:
                return
            visited_node.add(x.val)
            if x.val not in dic:
                dic[x.val] = Node(x.val)
            
            for neighbor in x.neighbors:
                if neighbor.val not in dic:
                    dic[neighbor.val] = Node(neighbor.val)
                (dic[x.val].neighbors).append(dic[neighbor.val])
                dfs(neighbor)
            return
        
        dfs(node)
        return dic[node.val]

