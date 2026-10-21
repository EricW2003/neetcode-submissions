from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visited = set()

        rottens = set()

        n, m = len(grid), len(grid[0])
        
        for i in range(n):
            for j in range(m):
                if grid[i][j]==2:
                    visited.add((i,j))
                    rottens.add((i,j))
                if grid[i][j] == 0:
                    visited.add((i,j))
        
        q = deque(rottens)
        t = 0
        while q:
            for _ in range(len(q)):
                i,j = q.popleft()

                nei = [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]

                for k,l in nei:
                    if k<n and l<m and k>=0 and l>=0 and (k,l) not in visited:
                        visited.add((k,l))
                        q.append((k,l))
            if q:
                t +=1
        if len(visited) == n*m:
            return t
        else:
            return -1







