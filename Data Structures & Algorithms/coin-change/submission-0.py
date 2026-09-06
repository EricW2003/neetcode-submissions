class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        ans = [0]*(amount+1)
        # if you start with $i dollars ans[i] is the minimal number of coins if order to obtain $amount
        
        # ans_i = 1+ min(ans_{i+coin} for coin in coins if i+coin<=amount)

        for i in range(amount-1,-1,-1):
            val = float("inf")
            for coin in coins:
                if i+coin <= amount:
                    val = min(val,1+ans[i+coin])
            ans[i] = val
        print(ans)
        return ans[0] if ans[0]!=float("inf") else -1