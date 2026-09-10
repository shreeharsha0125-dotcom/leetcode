class Solution(object):
    def twoSum(self, nums, target):

        seen = {}
        for i, x in enumerate(nums):
            com = target - x 

            if com in seen:
                return [ seen[com],i]
            else:
                seen[x] = i

           

nums = [2,7,11,15]
target = 9
obj = Solution()
print(obj.twoSum(nums,target))