class Solution(object):
    def singleNumber(self, nums):
        
        dir = {}

        for i in nums:
            if i not in dir:
                dir[i]  = 1 
            else:
                dir[i] += 1
        ans = min(dir, key=dir.get)
        return ans

nums = [2,2,1]
obj = Solution()
print(obj.singleNumber(nums))