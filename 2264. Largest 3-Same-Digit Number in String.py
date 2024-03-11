class Solution:
    def largestGoodInteger(self, num: str) -> str:
        

        variants = set()
        cnt = 0
        memorize1 = []

        for i in num:
            cnt += 1
            memorize1.append(i)
            if cnt >= 4:
                memorize1.pop(0)

            if len(set(memorize1)) == 1 and len(memorize1) == 3:
                variants.add(memorize1[0]*3)

        if variants:
            return (max(variants))
        else:
            return ''
            
print(Solution().largestGoodInteger(num = "230001119"))

        
            

'''
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        for i in range(9, -1, -1):
            candidate = str(i) * 3
            if candidate in num:
                return candidate
        return ""

А вот такой код в тупую просто побил 38ms
Beats 79.71%of users with Python3

я в ахуе
'''