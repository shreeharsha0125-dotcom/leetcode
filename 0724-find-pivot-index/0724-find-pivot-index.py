class Solution(object):
    def pivotIndex(self, nums):
        n = len(nums)
        pivot = -1
        prefix = [0]*len(nums)
        
        prefix[0] = nums[0]
        for i in range(1,n):
            prefix[i] = prefix[i-1] + nums[i]
        

        total_sum = prefix[-1]
        
        for i in range(n):
            if i > 0:
                left_sum = prefix[i-1]
            else:
                left_sum = 0

            right_sum = total_sum - left_sum - nums[i]
            if right_sum == left_sum:
                return i
            
        return pivot
    
nums = [2,1,-1]
obj = Solution()
print(obj.pivotIndex(nums))

