class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n=len(board)
        rows={i : set() for i in range(n)}
        cols={i : set() for i in range(n)}
        blocks={f"{i}{j}" : set() for i in range(3) for j in range(3)}
        print(blocks)

        for i in range(n):
            for j in range(n):
                digit=board[i][j]
                if board[i][j]!=".":
                    if digit in rows[i]:
                        return False
                    rows[i].add(digit)
                    if digit in cols[j]:
                        return False
                    cols[j].add(digit)
                    tier_i=i//3
                    tier_j=j//3
                    if digit in blocks[f"{tier_i}{tier_j}"]:
                        return False
                    blocks[f"{tier_i}{tier_j}"].add(digit)
        return True
