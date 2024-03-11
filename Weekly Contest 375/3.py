from typing import *
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        

        w_start = 0
        w_end = 0
        max_cnt = 0

        cnt = 0
        max_el = max(nums)
        

        while w_end < len(nums):

            if nums[w_end] == max_el:
                max_cnt += 1
            
            while max_cnt >= k:
                cnt += len(nums) - w_end

                if nums[w_start] == max_el:
                    max_cnt -= 1
                
                w_start += 1
            
            w_end += 1
        
        return cnt

