class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlength=0
        currlength=0
        leftp=0
        for i in range(len(s)):
            currlength+=1
            while leftp<i and s[i] in s[leftp:i]:
                leftp+=1
                currlength-=1
            maxlength=max(maxlength,currlength)
        return maxlength