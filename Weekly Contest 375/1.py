from typing import *
class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        
        temp_bat = [i for i in batteryPercentages]

        cnt = 0


        for i in range(len(batteryPercentages)):

            if temp_bat[i] > 0:
                cnt += 1
                temp_bat = [i-1 for i in temp_bat]

            else:
                continue

        return cnt 
    

print(Solution().countTestedDevices(batteryPercentages = [0, 1, 2]))