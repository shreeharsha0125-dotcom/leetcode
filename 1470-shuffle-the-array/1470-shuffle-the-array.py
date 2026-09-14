class Solution(object):
    def shuffle(self, nums, n):
        x = nums[:n]
        x1 = 0
        y = nums[n:]
        y1= 0
        ans = [0]*len(nums)
        for i in range(len(nums)):
            if i%2 == 0:
                ans[i]= x[x1]
                x1 += 1
            else:
                ans[i] = y[y1]
                y1 += 1 
        return ans
nums = [2,5,1,3,4,7]
n = 3
obj = Solution()
print(obj.shuffle(nums, n))