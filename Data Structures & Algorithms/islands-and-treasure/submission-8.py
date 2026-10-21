from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        zeros = []

        visited = set()

        n, m = len(grid), len(grid[0])

        for i in range(n):
            for j in range(m):
                if grid[i][j]==0:
                    zeros.append((i,j))
                    visited.add((i,j))
                if grid[i][j]==-1:
                    visited.add((i,j))
        q = deque(zeros)

        # q is the current points we are inspecting !!

        while q:
            new_set = set()
            for _ in range(len(q)):
                i,j = q.popleft()


                nei = [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]

                for k,l in nei:
                    if k>=0 and k<n and l>=0 and l<m and (k,l) not in visited:
                        grid[k][l] = min(grid[k][l],1+grid[i][j])
                        new_set.add((k,l))
            for k,l in new_set:            
                visited.add((k,l))
            q = deque(new_set)


