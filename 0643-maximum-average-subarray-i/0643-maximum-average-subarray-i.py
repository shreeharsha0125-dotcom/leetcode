class Solution(object):
    def findMaxAverage(self, nums, k):
        
        k_win = sum(nums[:k])
        maxi = k_win

        for i in range(k,len(nums)):
            k_win += nums[i]
            k_win -= nums[i-k]

            maxi = max(maxi, k_win)
        return float(maxi)/k

nums = [1,12,-5,-6,50,3] 
k = 4
obj = Solution()
print(obj.findMaxAverage(nums,k))