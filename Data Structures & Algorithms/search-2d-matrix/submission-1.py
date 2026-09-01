class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l=0
        m=len(matrix)
        n=len(matrix[0])
        r=m*n-1
        while l<r:
            mid=(l+r)//2
            row_mid,col_mid=self.int_to_coord(mid,n)
            if matrix[row_mid][col_mid]>=target:
                r=mid
            else:
                l=mid+1
        row_res,col_res=self.int_to_coord(l,n)
        return matrix[row_res][col_res]==target
    def int_to_coord(self,integer,n):
        #integer=k*n+(reminder of n) where k is the dividend
        return integer//n,integer%n
