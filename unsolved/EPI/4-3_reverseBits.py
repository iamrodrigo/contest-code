def numToInvert(num):
    a = int(0b1000000000000000)
    b = int(0b1)
    move = 15

    for _ in xrange(0, 8):
        endBit = (num & a) >> move
        begBit = (num & b) << move

        num = num | endBit if endBit != 0 else num ^ endBit
        num = num | begBit if begBit != 0 else num ^ begBit
        a >>= 1
        b <<= 1
        move -= 2
        print(bin(num))
        print('-----------------')

    return num

val = numToInvert(57345)
print(val, bin(val))
