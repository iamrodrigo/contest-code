class Solution(object):
    def reverseOnlyLetters(self, S):
        reversedStrind = list(S)
        reversedStack = []

        for c in S:
            if c.isalpha():
                reversedStack.append(c)

        if not len(reversedStack):
            return S

        for idx, c in enumerate(S):
            if c.isalpha():
                reversedStrind[idx] = reversedStack.pop()

        return  ''.join(reversedStrind)