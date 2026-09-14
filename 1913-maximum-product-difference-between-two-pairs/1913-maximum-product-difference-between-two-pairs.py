class Solution(object):
    def maxProductDifference(self, nums):
        nums.sort()
        a = nums[-1]
        b = nums[-2]
        c = nums[0]
        d = nums[1]
        return (a*b)-(c*d)
        
nums = [5,6,2,7,4]
obj = Solution()
print(obj.maxProductDifference(nums))