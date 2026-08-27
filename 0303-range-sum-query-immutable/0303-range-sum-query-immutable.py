class NumArray:

    def __init__(self, nums):
        
        self.prefix = [0] * len(nums)
        if nums:
            self.prefix[0] = nums[0]
            for i in range(1, len(nums)):
                self.prefix[i] = self.prefix[i-1] + nums[i]

    def sumRange(self, left , right) :
        if left == 0:
            return self.prefix[right]
        return self.prefix[right] - self.prefix[left-1]

numArray = NumArray([-2, 0, 3, -5, 2, -1])  
print(numArray.sumRange(0, 2))  
print(numArray.sumRange(2, 5))  
print(numArray.sumRange(0, 5))  
        


