from typing import *

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        
        return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    

print(Solution().transpose(matrix = [[1,2,3],[4,5,6]]))