from typing import *

class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        def is_substring(sub, s):
            return sub in s

        def get_shortest_non_substring(s, others):
            substrings = [s[i:j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)]
            substrings.sort()

            for sub in substrings:
                if all(not is_substring(sub, other) for other in others):
                    return sub

            return ''

        n = len(arr)
        answer = [''] * n

        for i in range(n):
            current_str = arr[i]
            others = arr[:i] + arr[i+1:]

            answer[i] = get_shortest_non_substring(current_str, others)

        return answer


print(Solution().shortestSubstrings(["fhi","ct","s","o","o"]))