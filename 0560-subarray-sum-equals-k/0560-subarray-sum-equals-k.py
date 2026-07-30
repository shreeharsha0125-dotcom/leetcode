class Solution:
    def subarraySum(self, nums, k):
        count = 0
        prefix_sum = 0
        prefix = {0: 1}

        for num in nums:
            prefix_sum += num

            if prefix_sum - k in prefix:
                count += prefix[prefix_sum - k]

            prefix[prefix_sum] = prefix.get(prefix_sum, 0) + 1

        return count


nums = [1, 1, 1]
k = 2

obj = Solution()
print(obj.subarraySum(nums, k))