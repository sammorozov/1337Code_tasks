class Solution:
    def largestOddNumber(self, num: str) -> str:
        

        for i in range(len(num)-1, -1, -1):

            if int(num[i]) % 2 == 1:

                return str(num[:i+1])
            
        else:
            return ''
        
print(Solution().largestOddNumber('42021361'))
        
