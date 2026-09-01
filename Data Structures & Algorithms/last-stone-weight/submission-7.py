class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        def aux(list_of_stones):
            if len(list_of_stones)==0:
                return 0

            if len(list_of_stones)==1:
                return list_of_stones[0] 

            a = list_of_stones[0]
            b = list_of_stones[1]
            if a>=b:
                first_place = (0,a)
                second_place = (1,b)
            else:
                first_place = (1,b)
                second_place = (0,a)
            for i in range(2,len(list_of_stones)):
                val = list_of_stones[i]
                if val > first_place[1]:
                    first_place, second_place = (i,val), first_place
                elif val >second_place[1]:
                    second_place = (i, val)
                else:
                    pass
            (i,val_i), (j, val_j) = first_place, second_place
            if val_i > val_j:
                    list_of_stones[i] = val_i-val_j
                    list_of_stones.pop(j)
            else:
                max_index, min_index = max(i,j), min(i,j)
                list_of_stones.pop(max_index)
                list_of_stones.pop(min_index)
            return aux(list_of_stones)
        return aux(stones)
