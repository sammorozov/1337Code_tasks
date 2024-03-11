from typing import *

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        
        common = 0
        for i in range(len(words)):
            for j in range(i, len(words)):

                if i == j :
                    continue
                if words[j].startswith(words[i]) and words[j].endswith(words[i]):
                    common += 1

        return common 

