class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        tab = [0] * n
        for i in range(1,n):
            for j in range(i):
                if tab[j]==0 and temperatures[i]>temperatures[j]:
                    tab[j]=i-j
        return tab

            


