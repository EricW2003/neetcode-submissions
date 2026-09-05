class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        # def aux(cards):
        #     if len(cards)<groupSize and cards:
        #         return False
        #     if not cards:
        #         return True
        #     nb = 1
        #     last_card = cards[0]
        #     remaining_cards = []
        #     for i in range(1,len(cards)):
        #         if nb<groupSize:
        #             if cards[i]>last_card+1:
        #                 return False
        #             elif cards[i]==last_card+1:
        #                 last_card+=1
        #                 nb+=1
        #             else:
        #                 remaining_cards.append(cards[i])
        #         else:
        #             remaining_cards.append(cards[i])
        #     return aux(remaining_cards)
        # return aux(hand)
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
        
        