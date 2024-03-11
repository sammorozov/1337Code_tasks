from typing import *

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        
        char_map = {}  # Mapping characters to their change costs
        for i in range(len(original)):
            char_map[original[i]] = char_map.get(original[i], {})
            char_map[original[i]][changed[i]] = min(char_map[original[i]].get(changed[i], float('inf')), cost[i])

        total_cost = 0
        i = 0
        while i < len(source):
            if source[i] != target[i]:
                if target[i] not in char_map.get(source[i], {}):
                    return -1  # Impossible to convert
                min_cost = char_map[source[i]][target[i]]
                j = i + 1
                while j < len(source) and source[j] == source[i]:
                    if target[j] not in char_map[source[j]]:
                        return -1  # Impossible to convert
                    min_cost = min(min_cost, char_map[source[j]][target[j]])
                    j += 1
                total_cost += min_cost * (j - i)
                i = j - 1
            i += 1

        return total_cost

solution = Solution()
print(solution.minimumCost("aaaa", "bbbb", ["a","c"], ["c","b"], [1,2]))  # Output: 12
