class Solution:
    def countPrimes(self, n: int) -> int:
        index = [1 for i in range(n)]
        nums = [i+1 for i in range(n)]

        for i in range(len(nums)):
            if index[i] == 0:
                continue
            if i == 0:
                index[i] = 0
                continue
            else:
                sdvig = nums[i]
                for s in range(sdvig*sdvig, n, sdvig):
                    index[s-1] = 0  # Adjust index to start from 0

        out = [nums[i] for i in range(len(nums)) if index[i] != 0]

        # print(out)

        return len(out) - 1

print(Solution().countPrimes(10))
