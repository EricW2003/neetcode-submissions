class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        def odd_search(i):
            length = 0
            while i-length-1>=0 and i+length+1<n and s[i-length-1]==s[i+length+1]:
                length+=1
            return length+1
        def pair_search(i):
            if i+1==n or s[i+1]!=s[i]:
                return 0
            length = 0
            while i-length-1>=0 and i+length+2<n and s[i-length-1]==s[i+length+2]:
                length+=1

            return 1+length

        ans = 0
        for i in range(n):
            ans = ans + odd_search(i) + pair_search(i)

        return ans