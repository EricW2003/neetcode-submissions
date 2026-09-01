class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n,m = len(grid), len(grid[0])
        starts = []
        # Find the rotten fruits and perfom last problem's notation changes
        for i in range(n):
            for j in range(m):
                if grid[i][j]==2:
                    starts.append((i,j))
                    grid[i][j]=0
                elif grid[i][j]==1:
                    grid[i][j]=2147483647
                else:
                    grid[i][j]=-1
        
        q = deque(starts)
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        max_val = 0
        #Find the maximum reached from the rotten fruits
        while q:
            node = q.popleft()
            for dx,dy in directions:
                i,j = node
                x,y = i+dx,j+dy
                if 0<=x<n and 0<=y<m and grid[x][y]==2147483647:
                        grid[x][y]= 1+grid[i][j]
                        max_val = max(max_val,grid[x][y])
                        q.append((x,y))
        # check is there is any unreached fruits
        for i in range(n):
            for j in range(m):
                if grid[i][j]==2147483647:
                    return -1
        return max_val

        # def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # n,m = len(grid), len(grid[0])
        # starts = []
        # # We need to find all the treseaures first and start from them
        # for i in range(n):
        #     for j in range(m):
        #         if grid[i][j]==0:
        #             starts.append((i,j))

        # q = deque(starts)
        # directions = [(0,1),(0,-1),(1,0),(-1,0)]
        # while q:
        #     node = q.popleft()
        #     for dx,dy in directions:
        #         i,j = node
        #         x,y = i+dx,j+dy
        #         if 0<=x<n and 0<=y<m and grid[x][y]==2147483647:
        #                 grid[x][y]= 1+grid[i][j]
        #                 q.append((x,y))

        # return 