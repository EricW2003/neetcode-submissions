class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(a):
            n = len(a)
            for i in range(n//2):
                if a[i] != a[n-1-i]:
                    return False
            return True

        if isPalindrome(s):
            return True
        
        for i in range(len(s)):
            if isPalindrome(s[:i]+s[i+1:]):
                return True
        return False
