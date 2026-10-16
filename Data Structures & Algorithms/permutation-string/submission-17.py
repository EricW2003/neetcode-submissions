class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        occ = [0]*26
        for letter in s1:
            occ[ord(letter)-ord("a")] += 1
        l = 0
        for r in range(len(s2)):
            occ[ord(s2[r])-ord("a")] -= 1

            while occ[ord(s2[r])-ord("a")] < 0 and l<=r:
                occ[ord(s2[l])-ord("a")] += 1
                l += 1
            
            if l<=r and occ == [0]*26:
                return True
        return False
