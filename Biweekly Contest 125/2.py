from typing import *

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        
        cnt = 0
        while min(nums) < k:

            a, b = nums[0], nums[1]
            nums.remove(a)
            nums.remove(b)

            temp_v = min(a, b) * 2 + max(a, b)


            for i in range(len(nums)-1):
                if temp_v <= min(nums):
                    nums.insert(0, temp_v)
                    break

                if temp_v >= max(nums):
                    nums.append(temp_v)
                    break

                if temp_v >= nums[i] and temp_v < nums[i+1]:
                    nums.insert(i+1, temp_v)
                    break
            else:
                if len(nums) == 0 or temp_v > max(nums) :
                    nums.append(temp_v)

                if len(nums) == 1:
                    nums.append(temp_v)
                    

            cnt += 1
            


        return cnt

print(Solution().minOperations([77,16,13,5], 78))


        

