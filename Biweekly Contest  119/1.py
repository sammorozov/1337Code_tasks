from typing import List

class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        s1 = set(nums1)
        s2 = set(nums2)
        
        cnums2 = sum(1 for n2 in nums1 if n2 in s2)
        cnums1 = sum(1 for n1 in nums2 if n1 in s1)
        
        return [cnums2, cnums1]

print(Solution().findIntersectionValues(nums1 = [3,4,2,3], nums2 = [1,5]))