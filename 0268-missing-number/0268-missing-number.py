class Solution(object):
    def missingNumber(self, nums):
        
        n = len(nums)
         
        for i in range(n+1):
            if i not in nums:
                return i
                
        
nums = [3,0,1]
obj = Solution()
print(obj.missingNumber(nums))

        