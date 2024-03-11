from typing import *

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        sum_of_k_first = sum(nums[:k])
        max_sum = sum_of_k_first
        for i in range(1, len(nums) - k + 1):
    
            sum_of_k_first = sum_of_k_first - nums[i-1] + nums[i+k-1]

            if sum_of_k_first > max_sum:
                max_sum = sum_of_k_first

            
        return max_sum / k
            
print(Solution().findMaxAverage(nums = [1,12,-5,-6,50,3], k = 4))



