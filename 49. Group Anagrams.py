from collections import Counter
from typing import *

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        cntrs = [Counter(s) for s in strs]

        big_smoke  = []

        out = dict()

        for i, j in zip(strs, cntrs):

            out[i] = j

        for string in strs:
            temp = []

            cnt = Counter(string) 

            for angrm, big_cnt in out.items():
                if big_cnt == cnt:
                    temp.append(angrm)
                    

            big_smoke.append(temp)



        
        return (big_smoke)

print(Solution().groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]))


'''
мега ГЕНИАЛЬНОЕ РЕШЕНИЕ!!!

'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {} 
        for s in strs:
            so ="".join(sorted(s)) 
            if so not in dict:
                dict[so] = [s] 
            else:
                dict[so].append(s)
        return dict.values()
        

        