class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return 0
        n = len(s)
        def odd_search(i):
            length = 0
            while i-length-1>=0 and i+length+1<n and s[i-length-1]==s[i+length+1]:
                length+=1
            return 1+2*length, i-length, i+length
        def pair_search(i):
            if i+1==n or s[i+1]!=s[i]:
                return 0, None, None
            length = 0
            while i-length-1>=0 and i+length+2<n and s[i-length-1]==s[i+length+2]:
                length+=1

            return 2+2*length, i-length, i+1+length
        max_length = 0
        max_left_index = None
        max_right_index = None

        for i in range(n):
            odd_length,odd_left,odd_right = odd_search(i)
            pair_length, pair_left, pair_right = pair_search(i)
            if odd_length > max_length:
                max_length = odd_length
                max_left_index = odd_left
                max_right_index = odd_right
            if pair_length > max_length:
                max_length = pair_length
                max_left_index = pair_left
                max_right_index = pair_right
        return s[max_left_index:max_right_index+1]
        
