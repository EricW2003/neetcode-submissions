class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False

        hash1={letter:0 for letter in s1}
        for letter in s1:
            hash1[letter]+=1
        n1=len(s1)
        h1=len(hash1)
        for i in range(n1):
            if s2[i] in hash1:
                hash1[s2[i]]-=1
        if list(hash1.values())==[0]*h1:
            return True
        for j in range(n1,len(s2)):
            if s2[j-n1] in hash1:
                hash1[s2[j-n1]]+=1
            if s2[j] in hash1:
                hash1[s2[j]]-=1
            if list(hash1.values())==[0]*h1:
                return True
        return False


