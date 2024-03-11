from typing import *



class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        
        nums = set([i+1 for i in range(len(grid)**2)])

        nums2 = []

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                nums2.append(grid[i][j])


        for i in range(len(nums2)):

            if nums2[i] in nums2[i+1:]:
                out = nums2[i]
                break



        a = [out]

        a += (list(nums - set(nums2)))
        
        return a



        


print(Solution().findMissingAndRepeatedValues(grid = [[9,1,7],[8,9,2],[3,4,6]]))