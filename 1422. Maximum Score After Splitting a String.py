class Solution:
    def maxScore(self, s: str) -> int:

        if len(set(s)) == 1:
            return len(s) - 1
        
        max_score = -float('inf')
        for i in range(1, len(s)):

            s1 = (s[0:i]).count('0')
            s2 = (s[i:]).count('1')

            if s1 + s2 > max_score:
                max_score = s1 + s2

        return max_score

print(Solution().maxScore("00"))

'''
норм решение про динамическое изменение макс суммы

class Solution:
    def maxScore(self, s: str) -> int:
        max_score = count_zeros_left = 0
        count_ones_right = s.count('1')

        for i in range(len(s) - 1):
            count_zeros_left += s[i] == '0'
            count_ones_right -= s[i] == '1'
            max_score = max(max_score, count_zeros_left + count_ones_right)

        return max_score

'''
