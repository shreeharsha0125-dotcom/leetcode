class Solution(object):
    def searchInsert(self, nums, target):
        
        if target in nums:
            left = 0
            rigth = len(nums) - 1
            ans = -1

            while left <= rigth:

                mid = (left + rigth)//2

                if nums[mid] == target:
                    ans = mid
                    break
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    rigth = mid - 1
            return ans
        else:
            nums.append(target)
            nums.sort()
            left = 0
            rigth = len(nums) - 1
            ans = -1

            while left <= rigth:

                mid = (left + rigth)//2

                if nums[mid] == target:
                    ans = mid
                    break
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    rigth = mid - 1
            return ans

nums = [-1,0,3,5,9,12]
target = 10
obj = Solution()
print(obj.searchInsert( nums, target))
           