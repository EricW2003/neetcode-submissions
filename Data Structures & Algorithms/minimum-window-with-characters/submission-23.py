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
        def is_contained(string):
            s_hash = string_to_hash(string)
            for letter in t:
                if letter not in s_hash or t_hash[letter]>s_hash[letter]:
                    return False
            return True
        for k in range(len(s)):
            for i in range(len(s)-k):
                if s[i] not in t or s[i+k] not in t:
                    pass
                else:
                    if is_contained(s[i:i+k+1]):
                        return s[i:i+k+1]
        return ""
                    


        



