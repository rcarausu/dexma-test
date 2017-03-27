def get_bytes(n):
    # considering 1 byte = 8 bits
    bits = 1
    do = True
    while do:
        low = -2 ** (bits - 1)
        high = 2 ** (bits - 1) - 1
        print('bits:{0}, low:{1}, high:{2}\n'.format(bits, low, high))
        if (low <= n and n <= high):
            do = False
        else:
            bits += 1

    if bits % 8 != 0:
        return bits//8 + 1
    else:
        return bits//8

print(get_bytes(32767))