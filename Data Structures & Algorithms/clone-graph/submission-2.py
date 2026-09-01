"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # from the dictionary, we can access every Node
        nodes = {}

        def dfs(node):
            # A visited Node exists AND has non empty current neighbors !

            if node.val in nodes and nodes[node.val].neighbors != []:
                return

            # To register the node is not added in the dictionary, it will be marked as visited once an neighbor is linked to it
            if node.val not in nodes:
                nodes[node.val]=Node(node.val)
            
            for nei in node.neighbors:
                #Register the neighbor in the dictinary if necessary
                if nei.val not in nodes:
                    nodes[nei.val]=Node(nei.val)
                # add the neighbor (and at the same time the main node will be marked as visited)
                nodes[node.val].neighbors.append(nodes[nei.val])
                # continue the process
                dfs(nei)
        if node is None:
            return None
        dfs(node)
        return nodes[1]


