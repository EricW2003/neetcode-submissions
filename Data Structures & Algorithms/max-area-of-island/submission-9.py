class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # visited = set()
        max_area = 0
        n , m =len(grid), len(grid[0])

        def dfs(i,j):
            if grid[i][j]==0:
                return
            nonlocal area 
            area += 1
            grid[i][j]=0

            
            #Search
            neis = []
            
            if i-1>=0:
                    neis.append((i-1,j))
            if i+1<n:
                    neis.append((i+1,j))
                
            if j-1>=0:
                    neis.append((i,j-1))
            if j+1<m:
                    neis.append((i,j+1))

            for nei in neis:
                k, l = nei
                if grid[k][l]==1:
                    dfs(k,l)

        for i in range(n):
            for j in range(m):
                node = (i,j)
                if grid[i][j]==1:
                    area = 0
                    dfs(i,j)
                    max_area = max(max_area, area)
        return max_area