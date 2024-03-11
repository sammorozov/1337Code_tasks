from typing import *



class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        
        nums = sorted(nums)

        out = []

        temp = []

        def check(args, key):
            
            a = args[0]
            b = args[1]
            c = args[2]
            k = key

            if abs(a - b) <= k and abs(a - c) <= k and abs(b - c) <= k:
                return True
            else:
                return False
 

        for i in range(len(nums)):

            if (i) % 3 == 0 and i != 0:
                out.append(temp)
                temp = []
                temp.append(nums[i])
            else:
                temp.append(nums[i])

            
        out.append(temp)

            

    
        for slce in out:
            
            if check(slce, k):
                continue
            else:
                return []
            

        return out

print(Solution().divideArray(nums = [1,3,3,2,7,3], k = 3))
             