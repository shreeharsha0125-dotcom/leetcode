class Solution(object):
    def subarraysDivByK(self, nums, k):

        remainder_count = {0: 1}  
        
        current_sum = 0
        result = 0
        
        for num in nums:
            current_sum += num
            remainder = current_sum % k
            if remainder in remainder_count:
                result += remainder_count[remainder]
                remainder_count[remainder] += 1
            else:
                remainder_count[remainder] = 1
                
        return result

nums = [4, 5, 0, -2, -3, 1]
k = 5
obj = Solution()
print(obj.subarraysDivByK(nums, k))  