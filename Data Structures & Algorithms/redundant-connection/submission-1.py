class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Union-Find
        n = len(edges)
        parent = list(range(n))
        size = [1] * n

        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]  # path compression
                x = parent[x]
            return x

        def union(a, b):
            ra = find(a-1)
            rb = find(b-1)

            if ra == rb:
                return False  # déjà connectés

            if size[ra] < size[rb]:
                ra, rb = rb, ra

            parent[rb] = ra
            size[ra] += size[rb]

            return True
        ans = []
        for a,b in edges:
            if not union(a,b):
                return [a,b]
        
        return ans[-1]
