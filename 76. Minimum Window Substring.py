class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def checker(s1, s2):
            # Check if all characters in s1 are present in s2 with required frequency
            for char, count in s1.items():
                if char not in s2 or s2[char] < count:
                    return False
            return True

        # Initialize character frequency dictionaries for t and the current window
        t_freq = {}
        window_freq = {}

        for char in t:
            t_freq[char] = t_freq.get(char, 0) + 1

        left = 0
        right = 0
        min_len = float('inf')
        result = ""

        while right < len(s):
            # Update window frequency for the current character
            window_freq[s[right]] = window_freq.get(s[right], 0) + 1
            right += 1

            # Check if the current window contains all characters from t
            while checker(t_freq, window_freq):
                # Update the minimum window length and result
                if right - left < min_len:
                    min_len = right - left
                    result = s[left:right]

                # Move the left pointer to shrink the window
                window_freq[s[left]] -= 1
                left += 1

        return result

# Test
print(Solution().minWindow(s="ADOBECODEBANC", t="ABC"))
