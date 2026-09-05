class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        dic = {}
        for card in hand:
            if card in dic:
                dic[card]+=1
            else:
                dic[card]=1
        
        while dic:
            x = min(dic)
            freq = dic[x]
            for i in range(groupSize):
                if x+i not in dic or dic[x+i]<freq:
                    return False
                dic[x+i]-=freq
                if dic[x+i]==0:
                    del dic[x+i]
        return True
        
        