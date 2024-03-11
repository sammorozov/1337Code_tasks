from typing import *

class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        
        res = []
        for i in range(1, len(mountain)-1):

            if mountain[i-1] < mountain[i] and mountain[i] > mountain[i+1]:
                res.append(i)

        return res
    

print(Solution().findPeaks(mountain = [2, 4, 4]))



