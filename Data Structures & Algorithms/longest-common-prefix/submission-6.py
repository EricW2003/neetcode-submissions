class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        curr_str = ""
        for i in range(len(strs[0])):
            target_str = strs[0][i]

            for j in range(1,len(strs)):
                test_str = strs[j]
                if len(test_str)< i+1:
                    return curr_str
                if not target_str == test_str[i]:
                    return curr_str
            
            curr_str+=target_str
        
        return curr_str
            