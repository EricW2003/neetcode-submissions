class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = [0]*26
        for i,letter in enumerate(s):
            d[ord(letter)-ord("a")]=i
            
        ans = []
        min_end = 0 
        start = 0
        for t, letter in enumerate(s):

            min_end = max(min_end, d[ord(letter)-ord("a")])
            
            if min_end == t:
                ans.append(min_end-start+1)
                start = t+1

        return ans