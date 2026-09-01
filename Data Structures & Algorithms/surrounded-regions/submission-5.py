class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited = set()
        n, m = len(board), len(board[0])
        def dfs():
            node = stack.pop()
            if node in visited:
                return 
            visited.add(node)
            i, j = node
            nonlocal not_surr
            if i==0 or i==n-1 or j==0 or j==m-1:
                not_surr = True
            directions = [(0,1),(0,-1),(1,0),(-1,0)]
            
            for dx,dy in directions:
                x, y = i+dx, j+dy
                if 0<=x<n and 0<=y<m and board[x][y]=="O":
                    stack.append((x,y))

        def dfs_2():
            node = stack.pop()
            i, j = node
            if board[i][j]=="X":
                return
            board[i][j]="X"
            directions = [(0,1),(0,-1),(1,0),(-1,0)]
            
            for dx,dy in directions:
                x, y = i+dx, j+dy
                if 0<=x<n and 0<=y<m and board[x][y]=="O":
                    stack.append((x,y))
        for i in range(n):
            for j in range(m):
                if board[i][j]=="O" and (i,j) not in visited:
                    not_surr = False
                    stack = [(i,j)]
                    while stack:
                        dfs()
                    if not not_surr:
                        stack = [(i,j)]
                        while stack:
                            dfs_2()
        return