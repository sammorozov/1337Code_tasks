from typing import *

class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        
        first = min(prices)
        prices.remove(first)
        second = min(prices)

        if second + first <= money:
            return money - first - second
        else:
            return money
        
print(Solution().buyChoco(prices = [1,1,0], money = 3))
