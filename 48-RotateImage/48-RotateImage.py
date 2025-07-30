# Last updated: 30/07/2025, 22:46:37
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        temp = [matrix[i].copy() for i in range(len(matrix)-1, -1, -1)]
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                matrix[i][j] = temp[j][i] 