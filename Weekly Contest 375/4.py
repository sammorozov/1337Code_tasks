from typing import List

class Solution:
    def numberOfGoodPartitions(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        n = len(nums)
        last_occurrence = {}
        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(1, n + 1):
            dp[i] = (2 * dp[i - 1]) % MOD
            if nums[i - 1] in last_occurrence:
                dp[i] -= dp[last_occurrence[nums[i - 1]]]
                dp[i] %= MOD
            last_occurrence[nums[i - 1]] = i - 1

        return (dp[n] - 1) % MOD

sol = Solution()
print(sol.numberOfGoodPartitions(nums=[1, 2, 3, 4]))
