class Solution(object):
    def removeDuplicates(self, nums):
        
        n = len(nums)
        result = []
        k = 0
        for i in nums:
           if i not in result:
                k += 1
                result.append(i)
        for i in range(len(result)):
            nums[i] = result[i]
        return k 
        
nums = [1,1,2]
obj = Solution()
print(obj.removeDuplicates(nums))