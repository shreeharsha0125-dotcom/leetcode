class Solution(object):
    def isAnagram(self, s, t):
        fq = {}
        for i in s:
            fq[i] = fq.get(i,0) + 1
        for i in t:
            fq [i] = fq.get(i,0) - 1
        for value in fq.values():
            if value != 0:
                return False
        return True
s = "anagram" 
t = "nagaram"
obj = Solution()
print(obj.isAnagram(s,t))          
        