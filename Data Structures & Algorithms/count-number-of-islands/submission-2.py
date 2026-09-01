class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # def dfs(node):
        #     if node in visited:
        #         return

        #     visited.add(node)

        #     for nei in graph[node]:
        #         dfs(nei)
        visited = set([])
        n_island = [0]
        n = len(grid)
        m = len(grid[0])
        def dfs(node, first_one): # first_one indicates if it's the first one encounterd looking for a new Island
            if node in visited:
                return
            print(node,first_one)
            visited.add(node)
            if first_one==1:
                # print(node)
                n_island[0] +=1
            
            #Search
            neis = []
            i, j = node
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
                if grid[k][l]=="1":
                    dfs(nei, 0)

        for i in range(n):
            for j in range(m):
                node = (i,j)
                if grid[i][j]=="1":
                    dfs(node, 1)
        print(visited)
        return n_island[0]