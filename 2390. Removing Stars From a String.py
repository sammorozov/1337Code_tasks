class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for i in s:
            if i != '*':
                stack.append(i)

            else:
                stack.pop()

        return ''.join(stack)
    
print(Solution().removeStars(s = "leet**cod*e"))