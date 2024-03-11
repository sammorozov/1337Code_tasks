from typing import List
import heapq as hq
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if len(nums)==1 and nums[0]>=k:return 0
        
        ans=0
        hq.heapify(nums)
        while(nums[0]<k and len(nums)>1):

            # когда мы попаем то тут сразуже идет ребалансировка кучи типа
            
            x=hq.heappop(nums) 
            y=hq.heappop(nums)
            tem=min(x, y) * 2 + max(x, y)
            hq.heappush(nums,tem)
            ans+=1
        
        
        
        return ans
    
print(Solution().minOperations(nums = [1,1,2,4,9], k = 20))