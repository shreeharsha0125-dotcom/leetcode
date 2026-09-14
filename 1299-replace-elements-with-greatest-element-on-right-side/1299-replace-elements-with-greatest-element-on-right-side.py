class Solution(object):
    def replaceElements(self, arr):
        ans = [-1]*len(arr)
        for i in range(len(arr)-1,0,-1):
            ans[i-1] = max(arr[i] , ans[i])
        return ans
arr = [17,18,5,4,6,1]

obj = Solution()
print(obj.replaceElements(arr))