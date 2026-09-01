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
        min_length = len(s)+1
        min_candidate = ""
        for i in range(len(s)):
            for j in range(i,len(s)):
                if s[i] not in t or s[j] not in t or j<i:
                    pass
                else:
                    if is_contained(s[i:j+1]) and len(s[i:j+1])<min_length:
                        min_length = len(s[i:j+1])
                        min_candidate = s[i:j+1]
        return min_candidate
                    


        



