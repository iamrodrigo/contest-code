class Solution(object):
    def toLowerCase(self, str):
        newString = ""
        for c in str:
            intOfC = ord(c)
            newString += chr(intOfC + 32) if 65 <= intOfC <= 90 else c

        return newString