class Solution:
    def incremovableSubarrayCount(self, nums):
        n = len(nums)
        count = 0
        left = [0] * n  # Array to store the number of elements to the left that can be included in an incremovable subarray
        right = [0] * n  # Array to store the number of elements to the right that can be included in an incremovable subarray
        
        # Count elements to the left
        for i in range(n):
            left[i] = i + 1
            while left[i] > 1 and (left[i] == i + 1 or nums[left[i] - 2] < nums[i]):
                left[i] -= 1
        
        # Count elements to the right
        for i in range(n - 1, -1, -1):
            right[i] = n - i
            while right[i] > 1 and (right[i] == n - i or nums[right[i] + i - 1] < nums[i]):
                right[i] -= 1
        
        # Calculate the total count of incremovable subarrays
        for i in range(n):
            count += left[i] * right[i]
        
        return count - n  # Subtract n for the single element subarrays

# Test cases
solution = Solution()
print(solution.incremovableSubarrayCount([1, 2, 3, 4]))  # Output: 10
print(solution.incremovableSubarrayCount([6, 5, 7, 8]))  # Output: 7
print(solution.incremovableSubarrayCount([8, 7, 6, 6]))  # Output: 3
