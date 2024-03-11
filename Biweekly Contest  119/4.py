from collections import defaultdict
from typing import List

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        fqs = defaultdict(int)
        left = 0
        max_l = 0

        for right, num in enumerate(nums):
            fqs[num] += 1
            
            while max(fqs.values()) > k:
                fqs[nums[left]] -= 1
                left += 1
            
            max_l = max(max_l, right - left + 1)
        
        return max_l

    
print(Solution().maxSubarrayLength(nums = [1,2,3,1,2,3,1,2], k = 2))
