class Solution:
    def numDecodings(self, s: str) -> int:        

        # if s[0]=="0":
        #     return 0
        
        # ans = self.numDecodings(s[1:])

        # if len(s)>=2:
        #     n = ord(s[0])-ord("0")
        #     n = 10*n+ord(s[1])-ord("0")
        #     if n<27:
        #         ans += self.numDecodings(s[2:])
        # return ans

        ans = [0]*len(s)

        if s[-1]!="0":
            ans[-1] = 1

        if len(s)==1:
            return ans[-1]

        if s[-2]!="0":
            ans[-2] += ans[-1]
            n = (ord(s[-2])-ord("0"))*10+(ord(s[-1])-ord("0"))
            if n < 27:
                ans[-2] += 1

        # two last digits are done
        for i in range(len(s)-3,-1,-1):
            if s[i]!="0":
                val = ans[i+1]
                n = (ord(s[i])-ord("0"))*10+(ord(s[i+1])-ord("0"))
                if n<27:
                    val += ans[i+2]
                ans[i] = val
        return ans[0]
        
        