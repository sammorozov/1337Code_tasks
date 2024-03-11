from typing import *

class Solution:
    def reverseVowels(self, s: str) -> str:
        
        vowels = {'A', 'a', 'O', 'o', 'U', 'u', 'E', 'e', 'I', 'i'}

        s = [i for i in s]

        right = 0
        left = len(s) - 1

        while right < left:

            if s[right] in vowels and s[left] in vowels:

                s[right], s[left] = s[left], s[right]
                left -= 1
                right += 1

            elif s[right] in vowels and s[left] not in vowels:
                left -= 1

            elif s[left] in vowels and s[right] not in vowels:
                right += 1

            else:
                left -= 1
                right += 1

        return ''.join(s)


print(Solution().reverseVowels(s = 'hello'))
print(Solution().reverseVowels(s = 'race car'))






