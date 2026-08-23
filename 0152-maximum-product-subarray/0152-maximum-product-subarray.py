class Solution:
    def maxProduct(self, nums):
        current_max = nums[0]
        current_min = nums[0]
        maximum = nums[0]

        for i in range(1, len(nums)):
            x = nums[i]

            if x < 0:
                current_max, current_min = current_min, current_max

            current_max = max(x, current_max * x)
            current_min = min(x, current_min * x)

            maximum = max(maximum, current_max)

        return maximum