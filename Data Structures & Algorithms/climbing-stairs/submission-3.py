class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        tab1 = 1
        tab2 = 2
        for i in range(2,n):
            tab2, tab1 = tab1+tab2, tab2
        return tab2