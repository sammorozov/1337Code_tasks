from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        out = ''
        dicks = dict(Counter(s))
        # print(dicks)
        sorted_dict_cnt = sorted(dicks, key=dicks.__getitem__, reverse=True)

        # print(sorted_dict_cnt)

        for i in sorted_dict_cnt:
            temp = i * dicks[i]
            out += temp

        return out
    
print(Solution().frequencySort('Aaba'))