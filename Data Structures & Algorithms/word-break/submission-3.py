class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)

        ans = [False]*(len(s)+1)
        ans[-1] = True

        # ans[i] is the output if s[i:] was the input 
        # ans[len(s)] will treated as the empty string

        for i in range(len(s)-1,-1,-1):
            substring = s[i:]
            for word in wordDict:
                if i+len(word) <=len(s) and substring[:len(word)] == word and ans[i+len(word)]:
                        ans[i] = True
                        break
            
        return ans[0]
            