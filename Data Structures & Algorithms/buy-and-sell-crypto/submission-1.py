class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_val=0
        max_price=prices[-1]
        for i in range(len(prices)-2,-1,-1):
            max_val=max(max_val,max_price-prices[i])
            max_price=max(max_price,prices[i])
        return max_val