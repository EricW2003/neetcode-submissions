class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s)!=len(t):
        #     return False
        # dic={}
        # for letter in s:
        #     if letter in dic:
        #         dic[letter]+=1
        #     else:
        #         dic[letter]=1
        # for letter in t:
        #     if letter in dic:
        #         dic[letter]-=1
        #     else:
        #         return False
        # for key in dic:
        #     if dic[key]!=0:
        #         return False
        # return True












        dic = {}
        for string in s:
            if string in dic:
                dic[string]+=1
            else:
                dic[string]=1
        
        for string in t:
            if string in dic:
                dic[string]-=1
            else:
                dic[string]=-1
        for key in dic:
            if dic[key]!=0:
                return False
        return True











