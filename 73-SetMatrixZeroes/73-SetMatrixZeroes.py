class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        idx = []
        for i in range(len(matrix)):
            if 0 in matrix[i]:
                for j, z in enumerate(matrix[i]):
                    if z == 0 and j not in idx:
                        idx.append(j)
                matrix[i] = [0] * len(matrix[i])

        for i in range(len(matrix)):
            for j in idx:
                matrix[i][j] = 0
                          
        