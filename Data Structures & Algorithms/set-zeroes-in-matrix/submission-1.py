class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row_index = set()
        col_index = set()

        for i in range((len(matrix))):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    row_index.add(i)
                    col_index.add(j)
        for i in range((len(matrix))):
            for j in range(len(matrix[0])):
                if i in row_index or j in col_index:
                    matrix[i][j] =0
        return

        