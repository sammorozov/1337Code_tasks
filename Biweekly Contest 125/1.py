from typing import *

class Solution:

    def minOperations(self, nums: List[int], k: int) -> int:
        
        cnt = 0 
        for i in nums:

            if i < k:
                cnt += 1

        return cnt
    
    