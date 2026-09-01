class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        tab = [0]*n
        tab[0] = 1
        tab[1] = 2
        for i in range(2,n):
            tab[i] = tab[i-1] + tab[i-2]
        return tab[-1]