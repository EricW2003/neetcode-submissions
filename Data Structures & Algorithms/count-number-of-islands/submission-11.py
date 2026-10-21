class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n,m = len(grid),len(grid[0])

        def dfs(k,l):
            if k<0 or l<0 or k>=n or l>=m or grid[k][l]=="0":
                return
            grid[k][l] = "0"

            dfs(k+1,l)
            dfs(k,l+1)
            dfs(k-1,l)
            dfs(k,l-1)
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]=="1":
                    ans += 1
                    dfs(i,j)
    
        return ans 