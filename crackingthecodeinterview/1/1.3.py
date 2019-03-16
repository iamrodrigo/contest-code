#1. Iterate string

def replaceSpaces(word, trueLength):
    spaceCount = 0

    for i in xrange(0, trueLength):
        if word[i] == ' ':
            spaceCount += 1

    index = trueLength + spaceCount * 2

    for i in xrange(trueLength - 1, 0, -1):
        if word[i] == ' ':
            word[index - 1] = '0'
            word[index - 2] = '2'
            word[index - 3] = '%'
            index -= 3
        else:
            word[index - 1] = word[i]
            index -= 1

    return word

print replaceSpaces(['M', 'r', ' ', 'J', 'o', 'h', 'n', ' ', 'S', 'm', 'i', 't', 'h', ' ', ' ', ' ', ' '], 13)