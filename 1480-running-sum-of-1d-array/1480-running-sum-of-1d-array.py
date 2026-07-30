class Solution():
    def runningSum(self, nums):
        ans = []
        running_sum = 0
        for num in nums:
            running_sum += num
            ans.append(running_sum)
        return ans
num = [1,2,3,4]
obj = Solution()
print(obj.runningSum(num))
        