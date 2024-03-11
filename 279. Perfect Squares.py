class Solution:
    def numSquares(self, n: int) -> int:
        

        our_ways = [i**2 for i in range(1, int(n ** (1/2)) + 1)][::-1]

        
        def return_coins(N):
            F = [0, 1]
            
            for i in range(2, N+1):
                new_value_list = []
                
                for coin in our_ways:
                    if i >= coin:
                        new_value_list.append(F[i-coin])
                F.append(1 + min(new_value_list))  

            return F[N]

        

        return return_coins(n)
    
print(Solution().numSquares(12))