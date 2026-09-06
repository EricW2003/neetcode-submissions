class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
            #  f = LCS
            # "cat"  "acccatct"
            # f("cat", "acccatct") = max("c" + f("at", "ccatct"), f("at", "acccatct") 
            # f(0, 0) =  max(1+f(1,firstoccurence of text1[0]+1), f(1, 0)
            #  i, j --> i+1, j and i+1, an index > j

            # f()

            #      (i,j)
                # (i+1,j)    (i+1, index>j)

            n, m = len(text1), len(text2)
            grid = [[0 for _ in range(m+1)] for _ in range(n+1)]

            grid[n-1][m-1] = 1 if text1[n-1]==text2[m-1] else 0

            for i in range(n-1,-1,-1):
                for j in range(m-1,-1,-1):
                    grid[i][j] = grid[i+1][j]
                    letter = text1[i]
                    firstoccurence = None

                    for k in range(j,m):
                        if text2[k]==letter:
                            firstoccurence = k
                            break

                    if firstoccurence is not None:
                        grid[i][j] = max(grid[i][j], 1+ grid[i+1][firstoccurence+1])
            print(grid)
            return grid[0][0]
