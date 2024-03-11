class Solution:
    def minOperations(self, s: str) -> int:
        
        str1 = [0 if i % 2 == 0 else 1 for i in range(len(s))]
        str2 = [1 if i % 2 == 0 else 0 for i in range(len(s))]

        print(str1)

        min_1 = 0
        min_2 = 0

        for i in range(len(s)):

            if str1[i] != int(s[i]):
                min_1 += 1

            if str2[i] != int(s[i]):
                min_2 += 1

        return min(min_1, min_2)

print(Solution().minOperations(s = "0100"))
