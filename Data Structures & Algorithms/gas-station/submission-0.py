class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        idx = 0
        curr_gas = 0
        for curr_idx in range(2*len(gas)):
            if idx == curr_idx-len(gas):
                return idx
            i = curr_idx % len(gas)
            curr_gas += gas[i]-cost[i]
            if curr_gas<0:
                idx = curr_idx+1
                curr_gas = 0
        return -1
    

