class Solution(object):
    def majorityElement(self, nums):
        nums.sort()
        data = {}
        for i in nums:
            if i not in data:
                data[i] = 1
            else:
                data[i] = data[i] + 1
        
        max_key = max(data, key=data.get)
        return max_key
nums = [3,2,3]
obj = Solution()
print(obj.majorityElement(nums))