class Solution:
    def maxFrequencyScore(self, nums, k):
        nums.sort()
        freq = {}
        left = 0
        max_freq = 0
        max_score = 0

        for right in range(len(nums)):
            freq[nums[right]] = freq.get(nums[right], 0) + 1
            max_freq = max(max_freq, freq[nums[right]])

            while (right - left + 1 - max_freq) > k:
                freq[nums[left]] -= 1
                left += 1

            max_score = max(max_score, min(right - left + 1, max_freq + k))

        return max_score


print(Solution().maxFrequencyScore(nums = [1,2,6,4], k = 3))