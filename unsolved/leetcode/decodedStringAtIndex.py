def decodeAtIndex(S, K):
    list = []
    for s in S:
        if s.isdigit():
            if len(list) * int(s) >= K:
                return list[(K % len(list)) - 1]
            else:
                list = list * int(s)
        else:
            list.append(s)

        if len(list) >= K:
            return list[K - 1]

print decodeAtIndex(raw_input(), input())