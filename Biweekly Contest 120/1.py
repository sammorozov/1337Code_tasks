from typing import List

class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        total_incremovable = 0
        n = len(nums)
        
        for i in range(n):
            left = 1
            while left <= i and nums[left - 1] < nums[left]:
                left += 1
            
            right = 1
            while i + right < n - 1 and nums[i + right] < nums[i + right + 1]:
                right += 1
            
            total_incremovable += left * right
        
        return total_incremovable

print(Solution().incremovableSubarrayCount(nums = [8,7,6,6]))