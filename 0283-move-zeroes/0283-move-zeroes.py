class Solution():
    def moveZeroes(self, nums):
        w = 0
        n = len(nums)
        
        for i in range(n):
            if nums[i] != 0:
                nums[w] = nums[i]
                w += 1
        
        while w < n:
            nums[w]  = 0          
            w += 1

        return nums

nums = [0,1,0,3,12]
obj = Solution()
print(obj.moveZeroes(nums))