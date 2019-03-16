def palindromePermutation(s):
    chars = set()
    for c in s:
        if c.isalpha():
            c = c.lower()
            if c in chars:
                chars.remove(c)
            else:
                chars.add(c)

    return False if len(chars) > 1 else True

print palindromePermutation("Tact Coa")
