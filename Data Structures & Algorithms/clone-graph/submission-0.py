"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        nodes = {}
        def dfs(node):
            if node.val in nodes and nodes[node.val].neighbors != []:
                return
            print("yes")
            if node.val not in nodes:
                nodes[node.val]=Node(node.val)
            
            for nei in node.neighbors:
                if nei.val not in nodes:
                    nodes[nei.val]=Node(nei.val)
                nodes[node.val].neighbors.append(nodes[nei.val])
                dfs(nei)
        if node is None:
            return None
        dfs(node)
        return nodes[1]


