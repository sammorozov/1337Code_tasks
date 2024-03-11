from typing import *

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        

        def first_pass(nums):

            left = 0
            right = len(nums) - 1
            min_left = nums[0]
            max_right = nums[len(nums) - 1]

            while left <= right:

                if nums[left] < nums[right]:
                    
                    if nums[left] < min_left:
                        min_left = nums[left]

                    if (min_left < nums[left] and nums[left] < max_right) or (min_left < nums[right] and nums[right] < max_right):
                        return True
                                
                    right -= 1


                if nums[left] > nums[right]:
                    
                    if nums[right] > max_right:
                        max_right = nums[right]

                    if (min_left < nums[left] and nums[left] < max_right) or (min_left < nums[right] and nums[right] < max_right):
                        return True
                                
                    left += 1

                if nums[left] == nums[right]:
                    if nums[right] > max_right:
                        max_right = nums[right]
                    if nums[left] < min_left:
                        min_left = nums[left]
                    if (min_left < nums[left] and nums[left] < max_right) or (min_left < nums[right] and nums[right] < max_right):
                        return True
                    
                    right -= 1
                    left += 1

            else:
                return False
            
        def second_pass(nums):
            left = 0
            right = len(nums) - 1
            min_left = nums[0]
            max_right = nums[len(nums) - 1]

            while left <= right:

                if nums[left] < nums[right]:
                    
                    if nums[left] < min_left:
                        min_left = nums[left]

                    if (min_left < nums[left] and nums[left] < max_right) or (min_left < nums[right] and nums[right] < max_right):
                        return True
                                
                    left += 1


                if nums[left] > nums[right]:
                    
                    if nums[right] > max_right:
                        max_right = nums[right]

                    if (min_left < nums[left] and nums[left] < max_right) or (min_left < nums[right] and nums[right] < max_right):
                        return True
                                
                    right -= 1

                if nums[left] == nums[right]:
                    if nums[right] > max_right:
                        max_right = nums[right]
                    if nums[left] < min_left:
                        min_left = nums[left]
                    if (min_left < nums[left] and nums[left] < max_right) or (min_left < nums[right] and nums[right] < max_right):
                        return True
                    
                    right -= 1
                    left += 1

            else:
                return False
            
        if second_pass(nums) or first_pass(nums):
            return True
        else:
            return False
        


        
print(Solution().increasingTriplet(nums = [20,100,10,12,5,13]))

'''
гениальное решение спизженное с литкода
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = float('inf')

        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True

        return False
        


'''