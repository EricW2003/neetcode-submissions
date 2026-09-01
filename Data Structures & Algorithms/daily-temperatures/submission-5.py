class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        tab = [[0] * n for _ in range(n)]
        for i in range(1,n):
            for j in range(i):
                if tab[i-1][j]==0 and temperatures[i]>temperatures[j]:
                    tab[i][j]=i-j
                else:
                    tab[i][j]=tab[i-1][j]
        return tab[-1]

            


