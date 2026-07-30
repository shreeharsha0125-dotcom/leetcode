class Solution():
    def finalValueAfterOperations(self, operations):
        x = 0
        for ope in operations:
            if(ope == "--X" or ope == "X--"):
                x -= 1
            if(ope == "++X" or ope == "X++"):
                x += 1
        return x
operations = ["--X","X++","X++"]
obj = Solution()
print(obj.finalValueAfterOperations( operations))