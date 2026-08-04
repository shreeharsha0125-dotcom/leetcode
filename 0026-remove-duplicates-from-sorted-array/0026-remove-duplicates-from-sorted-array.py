class Solution(object):
    def removeDuplicates(self, nums):
        n = len(nums)
        if n == 0 :
            return 0
        k = 1
        for i in range(1, n):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k += 1
        return k 
        
nums = [1,1,2]
obj = Solution()
print(obj.removeDuplicates(nums))