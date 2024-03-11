from typing import *

class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        

        nums_1 = sorted(nums, reverse=False)

        
        for i in range(0, len(nums) - 1, 2):


            nums_1[i], nums_1[i+1] = nums_1[i+1], nums_1[i]
            

        return nums_1
    
print(Solution().numberGame(nums = [5,4,2,3]))