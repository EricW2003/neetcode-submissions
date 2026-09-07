class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m, k = len(s1), len(s2), len(s3)
        if n+m!=k:
            return False

        grid = [[False for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]

        # grid[i][j] im currently at position i in s1 and position j in s2 and at position i+j-1 in s3 

        # grid[i][j] -> grid[i+1][j] if i+j <len(s3) and s3[i+j] == s1[i] 
        #  -> grid[i][j+1] if i+j <len(s3) and s3[i+j] == s1[j] 
        grid[0][0] = True

        for i in range(n+1):
            for j in range(m+1):
                if grid[i][j] and i+j<k:
                    if i<n and s3[i+j] ==s1[i]:
                        grid[i+1][j] = True
                    if j<m and s3[i+j] ==s2[j]:
                        grid[i][j+1] = True
        return grid[-1][-1]