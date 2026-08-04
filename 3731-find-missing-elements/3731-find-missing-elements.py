class Solution(object):
    def findMissingElements(self, nums):
        
        small = min(nums)
        larg = max(nums)
        out = []
        for i in range(small , larg+1):
            if i not in nums:
                out.append(i)
        return out
nums = [1,4,2,5]
obj = Solution()
print(obj.findMissingElements(nums))