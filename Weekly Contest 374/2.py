from typing import *


class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        
        maximum = 0
        coins = sorted(coins)

        ad_coins = 0
        while maximum < target:
            if len(coins) == 0 or coins[0] > maximum + 1:
                
                maximum += maximum + 1
                ad_coins += 1
            else:
                maximum += coins.pop(0)

        return ad_coins
    
print(Solution().minimumAddedCoins(coins = [1,4,10,5,7,19], target = 19))

