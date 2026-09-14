class Solution(object):
    def thirdMax(self, nums):
        seen = list(set(nums))
        seen.sort(reverse = True)
        if len(seen) < 3:
            return seen[0]
        return seen[2]
nums = [3,2,1]
obj = Solution()
print(obj.thirdMax(nums))