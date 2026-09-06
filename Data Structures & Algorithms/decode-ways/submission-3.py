class Solution:
    def numDecodings(self, s: str) -> int:        

        ans = [0]*(len(s)+1)
        ans[-1] = 1
        if s[-1]!="0":
            ans[-2] = 1

        for i in range(len(s)-2,-1,-1):
            if s[i]!="0":
                val = ans[i+1]
                n = (ord(s[i])-ord("0"))*10+(ord(s[i+1])-ord("0"))
                if n<27:
                    val += ans[i+2]
                ans[i] = val
                
        return ans[0]
        # s_i = (s[i] is non zero)*(s_i+1 + (s[i:i+2] is inferior to 27)*s_i+2)
        
        