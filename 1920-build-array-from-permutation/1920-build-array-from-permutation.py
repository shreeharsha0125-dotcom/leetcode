class Solution(object):
    def buildArray(self, nums):
        ans = [0]*len(nums)
        for i in range(len(nums)):
            ans[i] = nums[nums[i]]
        return ans
nums = [0,2,1,5,3,4]
obj = Solution()
print(obj.buildArray(nums))
        