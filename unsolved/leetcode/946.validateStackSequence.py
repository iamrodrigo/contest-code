class Solution(object):
    def validateStackSequences(self, pushed, popped):
        indexPopped = 0
        indexPushed = 0

        newStack = []

        while len(popped) != indexPopped:
            if len(newStack) and newStack[-1] == popped[indexPopped]:
                indexPopped += 1
                newStack.pop()
                continue

            while len(pushed) != indexPushed and popped[indexPopped] != pushed[indexPushed]:
                newStack.append(pushed[indexPushed])
                indexPushed += 1

            if len(pushed) == indexPushed:
                return False

            indexPopped += 1
            indexPushed += 1

        return True if not len(newStack) else False

s = Solution()
print s.validateStackSequences([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 9, 8, 7, 6, 5 ,4, 3, 2])






