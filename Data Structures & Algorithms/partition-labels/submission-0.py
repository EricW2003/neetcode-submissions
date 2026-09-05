class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = {}
        for i,letter in enumerate(s):
            d[letter]=i
        ans = []
        min_end = 0 
        start = 0
        for t, letter in enumerate(s):
            min_end = max(min_end, d[letter])
            
            if min_end == t:
                ans.append(min_end-start+1)
                start = t+1
        return ans