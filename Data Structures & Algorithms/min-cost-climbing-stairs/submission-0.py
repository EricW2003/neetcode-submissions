class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost)<2:
            return 0
        res = [-1]*len(cost)
        res[-1] = cost[-1]
        res[-2] = cost[-2]
        for i in range(len(res)-3,-1,-1):
            res[i] =cost[i]+ min(res[i+1],res[i+2])
        return min(res[0],res[1])