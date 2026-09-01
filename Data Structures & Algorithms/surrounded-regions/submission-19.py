class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited = set()
        n, m = len(board), len(board[0])
        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        for i in range(n):
            for j in range(m):
                if board[i][j] == "O" and (i, j) not in visited:
                    touches_border = False
                    stack = [(i, j)]
                    visited.add((i, j))
                    explored = []

                    while stack:
                        x, y = stack.pop()
                        explored.append((x, y))

                        if x == 0 or x == n-1 or y == 0 or y == m-1:
                            touches_border = True

                        for dx, dy in directions:
                            nx, ny = x + dx, y + dy

                            if (
                                0 <= nx < n
                                and 0 <= ny < m
                                and board[nx][ny] == "O"
                                and (nx, ny) not in visited
                            ):
                                visited.add((nx, ny))
                                stack.append((nx, ny))

                    if not touches_border:
                        for x, y in explored:
                            board[x][y] = "X"