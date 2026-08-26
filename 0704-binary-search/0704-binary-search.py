class Solution(object):
    def search(self, nums, target):
        
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
obj = Solution()
print(obj.search(nums , 9))
        