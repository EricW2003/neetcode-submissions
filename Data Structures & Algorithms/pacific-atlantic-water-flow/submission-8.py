class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n, m = len(heights), len(heights[0])

        visited_pacific = set()
        visited_atlantic = set()
        pacific = [[False for j in range(m)] for i in range(n)]
        atlantic = [[False for j in range(m)] for i in range(n)]
        for i in range(n):
            pacific[i][0]=True
            atlantic[i][m-1]=True
        for j in range(m):
            pacific[0][j]= True
            atlantic[n-1][j]=True
        def dfs_atlantic(node):
            if node in visited_atlantic:
                return
            visited_atlantic.add(node)
            i, j = node
            directions = [(0,1),(0,-1),(-1,0),(1,0)]
            for dx,dy in directions:
                x, y = i+dx,j+dy
                if 0<=x<n and 0<=y<m and heights[i][j]<=heights[x][y]:
                    atlantic[x][y]=True
                    dfs_atlantic((x,y))
        def dfs_pacific(node):
            if node in visited_pacific:
                return
            visited_pacific.add(node)
            i, j = node
            directions = [(0,1),(0,-1),(-1,0),(1,0)]
            for dx,dy in directions:
                x, y = i+dx,j+dy
                if 0<=x<n and 0<=y<m and heights[i][j]<=heights[x][y]:
                    pacific[x][y]=True
                    dfs_pacific((x,y))
        
        for i in range(n):
          for j in range(m):
            dfs_pacific((0,j))
            dfs_pacific((i,0))
            dfs_atlantic((n-1,j))
            dfs_atlantic((i,m-1))


        ans = []
        for i in range(n):
          for j in range(m):
            if pacific[i][j] and atlantic[i][j]:
              ans.append([i,j])

        return ans
