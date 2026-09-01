class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def string_to_hash(string):
            dic = {}
            for letter in string:
                if letter in dic:
                    dic[letter]+=1
                else:
                    dic[letter] = 1
            return dic
        t_hash = string_to_hash(t)
        def is_contained(s_h):
            for letter in t:
                if letter not in s_h or t_hash[letter]>s_h[letter]:
                    return False
            return True
        min_length = len(s)+1
        min_candidate = ""
        for i in range(len(s)):
            s_h ={}
            for j in range(i,len(s)):
                if s[j] in s_h:
                    s_h[s[j]]+=1
                else:
                    s_h[s[j]] = 1
                if s[i] not in t or s[j] not in t or j<i:
                    pass
                else:
                    if is_contained(s_h) and len(s[i:j+1])<min_length:
                        min_length = len(s[i:j+1])
                        min_candidate = s[i:j+1]
        return min_candidate

        # for k in range(len(s)):
        #     for i in range(len(s)-k):
        #         if s[i] not in t or s[i+k] not in t:
        #             pass
        #         else:
        #             if is_contained(s[i:i+k+1]):
        #                 return s[i:i+k+1]
        # return ""
                    


        



