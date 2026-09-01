class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def convert_to_arr(letters):
            dic=[0]*26
            for letter in letters:
                dic[ord(letter)-ord('a')]+=1
            return dic
        dic={}
        for string in strs:
            dic_string=convert_to_arr(string)
            if tuple(dic_string) in dic:
                dic[tuple(dic_string)].append(string)
            else:
                dic[tuple(dic_string)]=[string]
        return list(dic.values())