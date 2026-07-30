class Solution():
    def runningSum(self, nums):
        
        ans = []
        # ans.append(nums[0])
        for i in range(1,len(nums)+1):
            sum = 0
            for j in range(i):
                sum += nums[j] 
            ans.append(sum)
        return ans
num = [1,2,3,4]
obj = Solution()
print(obj.runningSum(num))
        