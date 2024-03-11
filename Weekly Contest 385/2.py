from typing import *

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        
        max_len = 0


        arr1 = sorted(arr1, key=lambda x: len(str(x)), reverse=True)
        arr2 = sorted(arr2, key=lambda x: len(str(x)), reverse=True)

        print(arr1)
        print(arr2)
        
        for num1 in arr1:
            for num2 in arr2:   

                common_len = 0

                num1_s = str(num1) 
                num2_s = str(num2)
                

                min_length = min(len(num1_s), len(num2_s))
                
                for i in range(min_length):
                    if num1_s[i] == num2_s[i]:
                        common_len += 1
                    else:
                        break

                if common_len > max_len:
                    max_len = common_len
                    return max_len
                    

        return max_len
    
print(Solution().longestCommonPrefix(arr1 = [1,3], arr2 = [32, 22]))