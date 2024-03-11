from typing import * 
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        
        a = set(nums1)
        b = set(nums2)

        return [list(a-b), list(b-a)]
    
print(Solution().findDifference(nums1 = [1,2,3], nums2 = [2,4,6]))