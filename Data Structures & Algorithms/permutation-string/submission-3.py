class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hash1={letter:0 for letter in s1}
        for letter in s1:
            hash1[letter]+=1

        if len(s1)>len(s2):
            return False
        for i in range(len(s1)):
            if s2[i] in hash1:
                hash1[s2[i]]-=1
        if list(hash1.values())==[0]*len(hash1):
            return True
        for j in range(len(s1),len(s2)):
            if s2[j-len(s1)] in hash1:
                hash1[s2[j-len(s1)]]+=1
            if s2[j] in hash1:
                hash1[s2[j]]-=1
            if list(hash1.values())==[0]*len(hash1):
                return True
        return False


