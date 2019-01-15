class Solution(object):
    def validateStackSequences(self, pushed, popped):
        indexPopped = 0
        newStack = []

        for i in pushed:
           newStack.append(i)

           while newStack and indexPopped < len(popped) and newStack[-1] == popped[indexPopped]:
               newStack.pop()
               indexPopped += 1

        return True if not len(newStack) else False

s = Solution()
print s.validateStackSequences([1,2,3,4,5], [4,5,3,2,1])