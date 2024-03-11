from typing import *

# class Solution:
#     def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        

#         for i in range(len(asteroids)):

#             if asteroids[i] < 0:

#                 j = i-1
#                 while j != 0:

#                     if asteroids[j] > 0:

#                         if abs(asteroids[i]) > abs(asteroids[j]):

#                             asteroids[j] = asteroids[i]

#                             asteroids[i] = 0

#                             j -= 1

#                         elif abs(asteroids[i]) < abs(asteroids[j]):

#                             asteroids[i] = 0

#                         else:
#                             asteroids[i] = 0
#                             asteroids[j] = 0

#         return asteroids
    
# print(Solution().asteroidCollision(asteroids = [10,2,-5]))







class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        result = []
        for i in asteroids:
            if i > 0:
                stack.append(i)
            elif i < 0 and len(stack) > 0:
                if stack[-1] > abs(i):
                    continue
                elif stack[-1] <= abs(i):
                    if stack[-1] == abs(i):
                        stack.pop()
                        break
                    else:
                        while stack[-1] < abs(i):
                            stack.pop()
                            if len(stack) == 0:
                                result.append(i)
                                break
                        if len(stack) != 0 and stack[-1] == abs(i):
                            stack.pop()
            elif i < 0 and len(stack) == 0:
                result.append(i)
        return result + stack









class Solution2:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stack = []

        for asteroid in asteroids:
            while stack and asteroid < 0 < stack[-1]:
                if stack[-1] < -asteroid:
                    stack.pop()
                    continue
                elif stack[-1] == -asteroid:
                    stack.pop()
                break
            else:
                stack.append(asteroid)

        return stack
    
print(Solution2().asteroidCollision(asteroids = [-2,2,1,-2]))
