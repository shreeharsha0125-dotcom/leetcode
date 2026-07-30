class Solution:
    def finalValueAfterOperations(self, operations):
        x = 0

        for ope in operations:
            if '+' in ope:
                x += 1
            else:
                x -= 1

        return x
operations = ["--X","X++","X++"]
obj = Solution()
print(obj.finalValueAfterOperations( operations))