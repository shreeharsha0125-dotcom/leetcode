class Solution(object):
    def threeSum(self, nums):
        ans = set()
        nums.sort()
        for i in range(len(nums)):
            left = i+1
            right = len(nums)-1

            while left < right:
                total = nums[i] + nums[right] + nums[left]

                if  total == 0:
                    ans.add((nums[i], nums[right], nums[left]))
                    left +=1
                    right -=1
                elif total  < 0:
                    left +=1
                else:
                    right -= 1
        return [list(triplet) for triplet in ans]

nums = [-1,0,1,2,-1,-4]
obj = Solution()
print(obj.threeSum( nums))
