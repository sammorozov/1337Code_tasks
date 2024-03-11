from typing import *
from collections import Counter



class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:

        finish_len = 0
        
        principal_cnt = Counter(chars)

        Flag = True

        for word in words:
            principal_word = Counter(word)
            for j in word:
                
                if (j in principal_cnt) and principal_cnt[j] >= principal_word[j]:
                    Flag = True
                
                else:
                    Flag = False
                    break

            if Flag:
                finish_len += len(word)

            else:
                Flag = True

        return finish_len

print(Solution().countCharacters(words = ["cat","bt","hat","tree"], chars = "atach"))



# '''
# придумаем алгоритм по быстрее
# '''


# from typing import *

# class Solution:
#     def countCharacters(self, words: List[str], chars: str) -> int:
#         length = []
#         for word in words:
#             for char in word:
#                 if chars.count(char) < word.count(char):
#                     break
#             else:
#                 length.append(len(word))
#         return sum(length)
    
# print(Solution().countCharacters(words = ["cat","bt","hat","tree"], chars = "atach"))
