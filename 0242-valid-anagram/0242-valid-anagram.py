class Solution(object):
    def isAnagram(self, s, t):
        s1 = sorted(s)
        t1 = sorted(t)
        if s1 == t1:
            return True
        else:
            return False
s = "anagram"
t = "nagaram"
obj = Solution()
print(obj.isAnagram)          
        