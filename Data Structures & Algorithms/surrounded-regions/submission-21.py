class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited = set()
        n, m = len(board), len(board[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        def dfs():
                node = stack.pop()
                if node in visited:
                    return 
                visited.add(node)
                
                a, b = node
                explored.append((a,b))
                
                nonlocal not_surr
                if a==0 or a==n-1 or b==0 or b==m-1:
                    not_surr = True
                
                for dx,dy in directions:
                    x, y = a+dx, b+dy
                    if 0<=x<n and 0<=y<m and board[x][y]=="O":
                        stack.append((x,y))

        for i in range(n):
            for j in range(m):
                if board[i][j]=="O" and (i,j) not in visited:
                    not_surr = False
                    stack = [(i,j)]
                    explored = []
                    while stack:
                        dfs()
                    if not not_surr:
                        for k,l in explored:
                            board[k][l]="X"
        return