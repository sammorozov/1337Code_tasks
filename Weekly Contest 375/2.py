
from typing import *
class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        good_ind = []
        for i, var_s in enumerate(variables):
            ai, bi, ci, mi = var_s
            if 0 <= ((ai ** bi % 10) ** ci) % mi == target:
                good_ind.append(i)
        return good_ind


print(Solution().getGoodIndices(variables = [[39,3,1000,1000]], target = 17))