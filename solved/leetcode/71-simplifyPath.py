list = []


def isValidSerialization(preorder):
    list = []
    for e in preorder.split(','):
        if e.isdigit():
            list.append(e)
        else:
            list.append(e)
            while len(list) > 2 and list[-1] == '#' and list[-2] == '#' and list[-3].isdigit():
                list.pop()
                list.pop()
                list.pop()
                list.append(e)

    return len(list) == 1 and list[0] == '#'




print isValidSerialization(raw_input())
