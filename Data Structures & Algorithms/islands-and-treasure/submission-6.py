from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n,m = len(grid), len(grid[0])
        starts = []
        # We need to find all the treseaures first and start from them
        for i in range(n):
            for j in range(m):
                if grid[i][j]==0:
                    starts.append((i,j))

        q = deque(starts)
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        while q:
            node = q.popleft()

            for dx,dy in directions:
                i,j = node
                x,y = i+dx,j+dy
                if 0<=x<n and 0<=y<m and grid[x][y]==2147483647:
                        grid[x][y]= 1+grid[i][j]
                        q.append((x,y))

        return 