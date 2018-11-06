import math

a = input()

for i in range(a):
    end, alf, gus = map(int, raw_input().split())

    beginning = 1
    count = int(math.log(end, 2))
    pointer = int(math.ceil(end // 2))
    while count != 1:
        if pointer % 2 != 0:
            pointer = pointer + 1

        if (pointer >= alf and pointer < gus) or (pointer >= gus and pointer < alf):
            break
        else:
            count = count - 1
            if pointer < alf and pointer < gus:
                beginning = pointer + 1
                pointer = pointer + ((end - pointer) // 2)
            else:
                end = pointer
                pointer = pointer - ((pointer + beginning) // 2)
    print count