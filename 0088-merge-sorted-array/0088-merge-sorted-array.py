class Solution(object):
    def merge(self, nums1, m, nums2, n):
        result = []
        if m != 0:
            for i in range(m):
                result.append(nums1[i])
        if n != 0 :
            for j in range(n):
                result.append(nums2[j])
        result.sort()
        for i in range(len(result)):
            nums1[i] = result[i]

        return result

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3   
obj = Solution()
print(obj.merge(nums1, m, nums2, n))    