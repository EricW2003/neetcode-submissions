class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        ans = [[0 for _ in range(len(coins)+1)] for _ in range(amount+1)]
        for i in range(len(coins)+1):
            ans[-1][i] = 1

        for i in range(amount-1,-1,-1):
            for j in range(len(coins),-1,-1):
                for k,coin in enumerate(coins):
                    if i+coin<=amount and (j==0 or coins[k]>=coins[j-1]):
                        ans[i][j] += ans[i+coin][k+1]
                
        return ans[0][0]