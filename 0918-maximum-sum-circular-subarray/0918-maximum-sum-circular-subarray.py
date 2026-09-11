class Solution(object):
    def maxSubarraySumCircular(self, nums):
      
        max_current = nums[0]
        max_global = nums[0]
        for i in range(1, len(nums)):
            max_current = max(nums[i], max_current + nums[i])
            max_global = max(max_global, max_current)

        min_current = nums[0]
        min_global = nums[0]
        for i in range(1, len(nums)):
            min_current = min(nums[i], min_current + nums[i])
            min_global = min(min_global, min_current)

        total_sum = sum(nums)

        if total_sum == min_global:
            return max_global
        else:
            return max(max_global, total_sum - min_global)


nums = [1, -2, 3, -2]
print(Solution().maxSubarraySumCircular(nums))  # Output: 3

   