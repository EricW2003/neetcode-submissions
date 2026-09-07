class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        # ans = [[0 for _ in range(len(coins)+1)] for _ in range(amount+1)]

        # for i in range(len(coins)+1):
        #     ans[-1][i] = 1

        # for i in range(amount-1,-1,-1):
        #     for j in range(len(coins),-1,-1):
        #         for k in range(max(j-1,0),len(coins)):
        #             coin = coins[k]
        #             if i+coin<=amount:
        #                 ans[i][j] += ans[i+coin][k+1]
        # return ans[0][0]

        # n = len(coins)
        # output = 0
        # def dfs(curr_amount,i):
        #     if curr_amount>=amount or i==n:
        #         nonlocal output
        #         if curr_amount==amount:
        #             output+=1
        #     k = 1
        #     while curr_amount + k*coins[i]<=amount:
        #         dfs(curr_amount + k*coins[i],i+1)
        # dfs(0,0)
        # return output

        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in range(len(coins) - 1, -1, -1):
            nextDP = [0] * (amount + 1)
            nextDP[0] = 1

            for a in range(1, amount + 1):
                nextDP[a] = dp[a]
                if a - coins[i] >= 0:
                    nextDP[a] += nextDP[a - coins[i]]
            dp = nextDP
        return dp[amount]


