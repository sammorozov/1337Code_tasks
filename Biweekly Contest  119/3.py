from typing import *
from collections import Counter
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        
        counter = Counter(nums)
        sorted_counter = sorted(counter.items(), key=lambda x: x[1])

        max_length = 0
        current_length = 0

        for num, freq in sorted_counter:
            if freq <= k:
                current_length += freq
            else:
                max_length = max(max_length, current_length)
                current_length = 0

        return max(max_length, current_length)
