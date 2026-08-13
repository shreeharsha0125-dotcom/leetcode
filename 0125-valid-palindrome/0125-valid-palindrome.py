class Solution(object):
    def isPalindrome(self, s):
        sh = ''.join(ch.lower() for ch in s if ch.isalnum() )

        left = 0
        right = len(sh) - 1

        while left < right:
            if sh[left] != sh[right]:
                return False

            left += 1
            right -= 1
        return True
s = "A man, a plan, a canal: Panama"
obj = Solution()
print(obj.isPalindrome(s))
        
        