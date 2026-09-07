class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==1:
            return 0

        maxprofit = 0

        ans = [0]*len(prices)
        ans[-1] = -prices[-1]
        ans[-2] = prices[-1]-prices[-2]

        maxprofit = max(maxprofit, ans[-1])
        maxprofit = max(maxprofit, ans[-2])

        max_list = [0]*(len(prices)+1)
        max_list[-2] = ans[-1]
        max_list[-3] = max(max_list[-1],ans[-2])

        for i in range(len(prices)-3,-1,-1):
            val = -prices[i]+prices[-1]
            for j in range(i+1,len(prices)-1):
                val = max(val,-prices[i]+prices[j]+max_list[j+2])
            ans[i] = val
            max_list[i] = max(max_list[i+1],val)
            maxprofit = max(maxprofit, ans[i])
        return maxprofit