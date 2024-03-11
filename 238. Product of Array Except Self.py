from typing import *

import functools



class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        a = [0] * len(nums)

        for i in range(len(nums)):

            lst = nums[:i] + nums[i+1:]

            a[i] = functools.reduce(lambda a, b : a * b, lst)

        return a
    

print(Solution().productExceptSelf(nums = [-1,1,0,-3,3]))



'''
это задача на динамическое программирование
'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)

        prefix_product = 1
        postfix_product = 1
        result = [0]*n
        
        for i in range(n):
            result[i] = prefix_product
            prefix_product *= nums[i]
        
        for i in range(n-1,-1,-1):
            result[i] *= postfix_product
            postfix_product *= nums[i]
        
        return result
    
print(Solution().productExceptSelf(nums = [1, 2, 3, 4]))
