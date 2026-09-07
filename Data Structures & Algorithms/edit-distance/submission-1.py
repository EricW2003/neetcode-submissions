class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        grid = [[0 for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]
        for i in range(len(word1)):
            grid[len(word1)-i-1][-1] = i+1
        for j in range(len(word2)):
            grid[-1][len(word2)-j-1] = j+1
        for i in range(len(word1)-1,-1,-1):
            for j in range(len(word2)-1,-1,-1):
                grid[i][j] = min(1+grid[i+1][j],1+grid[i][j+1])
                if word1[i] ==word2[j]:
                    grid[i][j] = min(grid[i][j],grid[i+1][j+1])
                else:
                    grid[i][j] = min(grid[i][j],grid[i+1][j+1]+1)
        return grid[0][0]
