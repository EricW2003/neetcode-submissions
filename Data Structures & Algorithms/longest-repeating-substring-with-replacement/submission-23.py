class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxlength=0
        if not s:
            return 0
        leftp=0
        hashmap={letter:0 for letter in s}
        most_freq=0
        for i in range(len(s)):
            hashmap[s[i]]+=1
            if hashmap[s[i]]>most_freq:
                most_freq=hashmap[s[i]]
            while i-leftp+1-most_freq>k:
                hashmap[s[leftp]]-=1
                leftp+=1    
            n=i-leftp+1
            maxlength=max(maxlength,n)
        return maxlength
