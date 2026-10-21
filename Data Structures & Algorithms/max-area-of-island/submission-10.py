class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n,m = len(grid),len(grid[0])

        def dfs(k,l):
            if k<0 or l<0 or k>=n or l>=m or grid[k][l]==0:
                return
            grid[k][l] = 0
            nonlocal curr_area
            curr_area += 1
            dfs(k+1,l)
            dfs(k,l+1)
            dfs(k-1,l)
            dfs(k,l-1)
        max_area = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    curr_area = 0
                    dfs(i,j)
                    max_area = max(max_area,curr_area)

        return max_area 