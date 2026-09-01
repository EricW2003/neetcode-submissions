class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        sol = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(n):
            sol[-1][i]=1
        for j in range(m):
            sol[j][-1]=1
        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                sol[i][j]=sol[i+1][j]+sol[i][j+1]
        return sol[0][0]
        