class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        n, m = len(grid), len(grid[0])
        n_island = 0

        def dfs(i, j):
            if (i, j) in visited:
                return

            visited.add((i, j))

            directions = [(1,0), (-1,0), (0,1), (0,-1)]

            for di, dj in directions:
                ni, nj = i + di, j + dj

                if 0 <= ni < n and 0 <= nj < m:
                    if grid[ni][nj] == "1":
                        dfs(ni, nj)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1" and (i, j) not in visited:
                    n_island += 1
                    dfs(i, j)

        return n_island