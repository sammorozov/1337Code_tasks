from typing import List

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        def find_shortest_length(strings):
            return len(min(strings, key=len))

        def all_contain_prefix(strings, prefix, start, end):
            for i in range(0, len(strings)):
                word = strings[i]
                for j in range(start, end + 1):
                    if word[j] != prefix[j]:
                        return False
            return True

        def find_longest_common_prefix_pair(x, y):
            shortest_length = min(len(x), len(y))
            common_prefix = ""

            low, high = 0, shortest_length - 1
            while low <= high:
                mid = int(low + (high - low) / 2)
                if all_contain_prefix([x, y], x, low, mid):
                    common_prefix = common_prefix + x[low:mid + 1]
                    low = mid + 1
                else:
                    high = mid - 1

            return common_prefix

        max_common_prefix = 0

        for x in arr1:
            for y in arr2:
                common_prefix = find_longest_common_prefix_pair(str(x), str(y))
                max_common_prefix = max(max_common_prefix, len(common_prefix))

        return max_common_prefix
    
print(Solution().longestCommonPrefix(arr1 = [1,2,3], arr2 = [4,4,4]))