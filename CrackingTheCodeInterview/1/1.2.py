# 1. Check if the length is the same
# 2. one variable, the len(), called x
# 3. A foor loop where we iterate any word. We'll take the last char of the second word and compare with the current
# char of the first word. if they are different, return false. decrease 1 x and repeat
# if it finishes the loop, return true

def permutationOfOther(wordOne, wordTwo):

    if len(wordTwo) != len(wordOne):
        return False

    x = len(wordOne) - 1

    for c in wordTwo:
        if c != wordOne[x]:
            return False
        x -= 1

    return True

print permutationOfOther(raw_input(), raw_input())