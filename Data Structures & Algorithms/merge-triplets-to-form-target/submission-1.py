class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # max(max(a,b),c) = max(a,b,c)

        # first step: cleaning
        # clean the triplets where (x < x_i or y < y_i or z<z_i)
        # x < x_i

        x,y,z = target[0],target[1],target[2]
        # searching for triplets where x_i = x, y_i =y, z_i = z 
        x_bool = False
        y_bool = False
        z_bool = False
        for triplet in triplets:
            x_i,y_i,z_i = triplet[0],triplet[1],triplet[2]
            if x_i<=x and y_i<=y and z_i<=z:
                if x_i==x:
                    x_bool = True
                if y_i==y:
                    y_bool = True
                if z_i==z:
                    z_bool = True
            if x_bool and y_bool and z_bool:
                return True
        return False
        # x_i < x

