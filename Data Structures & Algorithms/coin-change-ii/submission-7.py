class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        ans = [[0 for _ in range(len(coins)+1)] for _ in range(amount+1)]

        for i in range(len(coins)+1):
            ans[-1][i] = 1

        for i in range(amount-1,-1,-1):
            for j in range(len(coins),-1,-1):
                for k in range(max(j-1,0),len(coins)):
                    coin = coins[k]
                    if i+coin<=amount:
                        ans[i][j] += ans[i+coin][k+1]
        return ans[0][0]

