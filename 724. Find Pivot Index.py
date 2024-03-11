# from typing import *

# class Solution:
#     def pivotIndex(self, nums: List[int]) -> int:
        
#         left = 0
#         right = len(nums) - 1

#         left_sum = nums[left]
#         right_sum = nums[right]

#         while left < right:

#             if left_sum < right_sum:

#                 left += 1

#                 left_sum += nums[left]
            
#             elif left_sum > right_sum:

#                 right -= 1

#                 right_sum += nums[right]

#             else:
#                 right -= 1
#                 right_sum += nums[right]
                
        

#         if left_sum == right_sum:
#             return left
#         else:
#             return -1

# print(Solution().pivotIndex([1,7,3,6,5,6]))

from typing import *

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        n = len(nums)
        prefix_1 = [0] * (n+1)

        prefix_2 = [0] * (n+1)

        for i in range(1, n+1):
            prefix_1[i] = prefix_1[i-1] + nums[i-1]

        nums = nums[::-1]

        for i in range(1, n+1):
            prefix_2[i] = prefix_2[i-1] + nums[i-1]

        print(prefix_1)
        print(prefix_2)


        del prefix_1[0]

        del prefix_2[::-1][-1]

        print(prefix_1)
        print(prefix_2)

        for i in range(n):
            if prefix_1[i] == prefix_2[i]:
                return i
        else:
            return -1 
        
print(Solution().pivotIndex([1,7,3,6,5,6]))