class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        first_str = strs[0]
        for i in range(len(first_str)):
            target_letter = first_str[i]
            
            for j in range(1,len(strs)):
                test_str = strs[j]

                if len(test_str) < i+1:
                    return first_str[:i]

                if not  target_letter == test_str[i]:
                    return first_str[:i]

        
        return first_str
            