class Solution:
    def totalMoney(self, n: int) -> int:
        
        prod = 1
        summ = 0
        week = 0
        for i in range(1, n+1):
            summ += prod + week
            prod += 1


            if i % 7 == 0:
                week += 1
                prod = 1

            

        return summ 


print(Solution().totalMoney(10))